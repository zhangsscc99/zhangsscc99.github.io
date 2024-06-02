import { useRef } from "react"

function App () {
    const inputRef = useRef(null)
    const showDom = () => {
        console.log(inputRef.current)
    }
    return (
        <div>
            <input ref={inputRef} type="text" />
            <button onClick={showDom}>Show DOM</button>
        </div>
    )
}