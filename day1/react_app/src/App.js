import { useSelector, useDispatch } from "react-redux";

function App() {

  const modifyColor = useSelector( (state)=>state.modifyColor )
  const dispatch = useDispatch()

  return (
    <div className="App container-fluid">
      <section style={{backgroundColor:modifyColor }} className='vh-100 border d-flex flex-column justify-content-center align-items-center'>
        <div >
          <button onClick={ ()=>{dispatch({type: "CHANGE COLOR"})} } className='p-3 m-3'>Change</button>
        </div>
        <div>
          rgb({modifyColor})
        </div>
        
      </section>
    </div>
  );
}

export default App;
