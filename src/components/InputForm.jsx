import { useState } from 'react'
import { clubs } from '../data/clubs.js'



function InputForm({ onSave, selectedClub, onClubChange, records  }) {

    const [distance, setDistance] = useState('')
    const handleSave = () => {
        
        if(distance === ''){
            alert ("数値を入力してください")
            return false;
        } else if(isNaN(distance)) {
            alert ("数値を入力してください")
            return false;
        } else if(Number(distance) <= 0) {
            alert ("ミスショットは打ち直してください")
            return false;
        }
    
        const clubRecords = records.filter((r) => r.club === selectedClub)
        const strokeNumber = clubRecords.length + 1

        const newRecord = {
            id: Date.now(),
            club: selectedClub,
            distance: Number(distance),
            strokeNumber: strokeNumber,
            day: new Date().toISOString().slice(0, 10)
        }

        localStorage.setItem('records', JSON.stringify([...records, newRecord]))

        setDistance('')

        onSave([...records, newRecord])

        return true;
        
    }

    const handleClubChange = (e) => {
        onClubChange(e.target.value)
    }

    return (
        <div className="input-card">
            <div className="input-row">
                <select value={selectedClub} onChange={handleClubChange}>
	                {clubs.map((club) => (
  				        <option key={club} value={club}>{club}</option>
			        ))}
                </select>
                <input type="number" value={distance} onChange={(e) => setDistance(e.target.value)}>
                </input>
                <button onClick={handleSave}>保存</button>
                
            </div>
        </div>
    )
}



export default InputForm