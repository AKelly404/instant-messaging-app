import { useEffect, useState } from 'react'
import './App.css'
import {ThreadService} from '../services/thread.service'
import { Thread } from '../models/thread'

function App() {
  const [data, setData] = useState<Thread[]>([])
  const renderThreads = () => {
    return data.map((element) => {
      return <li key={element.createdAt}>{element.createdAt}</li>
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