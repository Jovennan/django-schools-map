import axios from 'axios'
import {Icon} from 'leaflet'
import React, {useState} from 'react'
import {Alert, Spinner} from 'react-bootstrap'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import useSWR from 'swr'
import './App.css'

export const icon = new Icon({
  iconUrl: 'leaf-green.png',
  shadowUrl: 'leaf-shadow.png',
  iconSize: [38, 95],
  shadowSize: [50, 64],
  iconAnchor: [22, 94],
  shadowAnchor: [4, 62],
  popupAnchor: [-3, 76],
})

const fetcher = (url) => axios.get(url).then((res) => res.data)

const App = () => {
  const [activeSchool, setActiveSchool] = useState(null)
  const {data, error} = useSWR("/api/v1/schools", fetcher)
  const schools = data && !error ? data : {}
  const position = [-7.12,-34.89]
  const zoom = 10

  if (error) {
    return <Alert variant='danger'>We have a problem</Alert>
  }
  if (!data) {
    return (
      <Spinner
        animation='border'
        variant='danger'
        role='status'
        style={{
          width: '400px',
          height: '400px',
          margin: 'auto',
          display: 'block',
        }}
      />
    )
  }
  return (
    <MapContainer center={position} zoom={zoom}>
      <TileLayer 
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {schools.features.map((school)=>(
        <Marker
          key={school.properties.name}
          position={[
            school.geometry.coordinates[1],
            school.geometry.coordinates[0],
          ]}
          onClick={()=>{
            setActiveSchool(school)
          }}
          icon={icon}
        >
          <Popup
            position={[
              school.geometry.coordinates[1],
              school.geometry.coordinates[0],
            ]}
            onClose={()=>{
              setActiveSchool(null)
            }}
          >
            <div>
              <h6>{school.properties.name}</h6>
              <p>{school.properties.regional}</p>
              <p>{school.properties.level}</p>
              <p>{school.properties.governance}</p>
            </div>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  )
}

export default App