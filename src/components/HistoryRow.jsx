function HistoryRow({ record, onDelete }) {
  return (
    <div className="history-row">
      <div className="history-info">
        <span className="stroke-number">{record.strokeNumber}球目</span>
        <span className="stroke-distance">{record.distance}yds</span>
        <span className="stroke-day">{record.day}</span>
      </div>
      <button className="delete-btn" onClick={() => onDelete(record.id)}>削除</button>
    </div>
  )
}

export default HistoryRow