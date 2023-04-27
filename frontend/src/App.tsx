import { useEffect, useState } from 'react'
import './App.css'
import {ThreadService} from '../services/thread.service'

function App() {
  const [data, setData] = useState([])
  const renderThreads = () => {
    return data.map((element) => {
      return <li key={element.created_at}>{element.created_at}</li>
    })
  }
  useEffect(() => {
      const fetchData = async () => {
      const threadService = new ThreadService()
      setData(await threadService.getAll());
    }
    fetchData()
      .catch(console.error);
  }, [])
  return (
    <>
      <ul>
        {renderThreads()}
      </ul>
    </>
  )
}

export default App