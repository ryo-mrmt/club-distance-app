import { clubs } from '../data/clubs.js'
import ClubRow from './ClubRow.jsx'

function ClubList({records = [], selectedClub, onDelete, onDeleteAll }) {

  const getAverage = (clubName) => {
    const clubRecords = records.filter((record) => record.club === clubName)
    const sorted = clubRecords.sort((a,b) => b.id - a.id).slice(0, 3)
    const total = sorted.reduce((sum, record) => sum + record.distance, 0)
    return sorted.length > 0 ? total / sorted.length : 0
  }

  const activeClubs = clubs.filter((club) => 
    records.some((r) => r.club === club)
  )

  const currentIndex = activeClubs.indexOf(selectedClub)
  const average = getAverage(selectedClub)
  const range = [-2, -1, 1, 2]
  const neighbors = range
    .map((offset) => {
      const i = currentIndex + offset
      if (i < 0 || i >= activeClubs.length) return null
      const name = activeClubs[i]
      return {
        club: name,
        avg: getAverage(name),
        diff: getAverage(name) - average
      }
    })
  .filter((n) => n !== null)

  return (
    <div>
      <ClubRow 
        selectedClub={selectedClub} 
        average={average} 
        neighbors={neighbors}
        records={records}
        onDelete={onDelete}
        onDeleteAll={onDeleteAll}
      />
      
    </div>
  )
}

export default ClubList