import { Thread } from "../../../models/thread"

interface ThreadCardProps {
    thread: Thread
    onClick: (id: string) => void //void is the return type 
}

function ThreadCard(properties: ThreadCardProps) {
    return (
    <div className='thread' key={properties.thread.id} onClick={() => properties.onClick(properties.thread.id)}>
        <div>{properties.thread.id}</div>
        <div>{properties.thread.lastUsedAt}</div>
    </div>
    )
}

export default ThreadCard