import { useEffect, useState } from 'react'
import './App.css'
import {ThreadService} from '../services/thread.service'
import { Thread } from '../models/thread'
import ThreadCard from './components/threads-card/thread-card'

function App() {
  const [data, setData] = useState<Thread[]>([])
  const renderThreads = () => {
    return data.map((element) => {
      return <ThreadCard key={element.id} thread={element}></ThreadCard>
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