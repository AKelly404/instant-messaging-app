import { useEffect, useState } from 'react'
import './App.css'
import {ThreadService} from '../services/thread.service'
import { Thread } from '../models/thread'
import { Message } from '../models/message'
import ThreadCard from './components/threads-card/thread-card'
import MessageList from './components/message-list/message-list'

function App() {
  const [data, setData] = useState<Thread[]>([])
  const [messagesData, setMessagesData] = useState<Message[]>([])
  const renderThreads = () => {
    return data.map((element) => {
      return <ThreadCard key={element.id} thread={element} onClick={renderMessages}></ThreadCard>
    })
  }
  const renderMessages = () => {
    return messagesData.map((element) => {
      return <MessageList key={element.id} message={element}></MessageList>
    })
  }
  useEffect(() => { //this executes everytime the something in the second para changes
    const fetchData = async () => {
      const threadService = new ThreadService()
      if (data.length == 0) {
        setData(await threadService.getAll()); //used to modify data var
      }
      if (data.length !== 0) {
        setMessagesData(await threadService.getMessages(data[0].id));
      }
    }
    fetchData()
      .catch(console.error);
  }, [data])
  return (
    <>
    <div className='container'>
      <div className='threadSidebar'>
        {renderThreads()}
      </div>
      <div className='messageBox'>
        {renderMessages()}
      </div>
    </div>
    </>
  )
}

export default App