import { useEffect, useState } from 'react'
import './App.css'
import {ThreadService} from '../services/thread.service'
import { Thread } from '../models/thread'

function App() {
  const [data, setData] = useState<Thread[]>([])
  const renderThreads = () => {
    return data.map((element) => {
      return <div className='thread' key={element.id}>
                <div>{element.id}</div>
                <div>{element.lastUsedAt}</div>
              </div>
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
    <div className='container'>
      <div className='threadSidebar'>
        {renderThreads()}
      </div>
    </div>
    </>
  )
}

export default App