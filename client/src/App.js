import React from 'react'
import { MapContainer, TileLayer } from 'react-leaflet'
import './App.css'

const App = () => {
  return (
    <MapContainer center={[-7.1281874,-34.8944061]} zoom={9}>
      <TileLayer 
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
    </MapContainer>
  )
}

export default App