import InputForm from './components/InputForm.jsx'
import ClubList from './components/ClubList.jsx'
import { useState } from 'react'


function App() {
  const [records, setRecords] = useState(
  JSON.parse(localStorage.getItem('records') || '[]')
  )
  const [selectedClub, setSelectedClub] = useState('1W')

  const handleDelete = (id) => {
    const updated = records.filter((r) => r.id !== id)
    localStorage.setItem('records', JSON.stringify(updated))
    setRecords(updated)
  }

  const handleDeleteAll = (clubName) => {
    const updated = records.filter((r) => r.club !== clubName)
    localStorage.setItem('records', JSON.stringify(updated))
    setRecords(updated)
  }

  return (
    <div>
      <h1>クラブ飛距離メモ</h1>
      <InputForm 
        onSave={(newRecords) => setRecords(newRecords)} 
        selectedClub={selectedClub} 
        onClubChange={(club) => {setSelectedClub(club)}} 
      />
      <ClubList 
        records={records} 
        selectedClub={selectedClub} 
        onDelete={handleDelete} 
        onDeleteAll={handleDeleteAll}
      />
    </div>
  )
}

export default App