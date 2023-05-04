import { Thread } from "../../../models/thread"

interface ThreadCardProps {
    thread: Thread
}

function ThreadCard(properties: ThreadCardProps) {
    return (
    <div className='thread' key={properties.thread.id}>
        <div>{properties.thread.id}</div>
        <div>{properties.thread.lastUsedAt}</div>
    </div>
    )
}

export default ThreadCard