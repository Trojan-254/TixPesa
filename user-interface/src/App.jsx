// import UserAuthentication from "./components/UserAuthentication"
import Register from "./components/Register"
const App = () => {
  return (
    <div className="flex w-full h-screen">
      <div className="items-center justify-center h-320 flex lg:w-1/2 bg-gray-100">
      {/* <UserAuthentication/> */}
      <Register/>
      </div>
      <div className="hidden relative lg:flex h-full w-1/2 items-center justify-center bg-gray-200">
        <div className="w-60 h-60 bg-gradient-to-tr from-violet-500 to-pink-500 rounded-full animate-bounce">
            <p className="text-center items-center mt-5 text-5xl font-bold line-clamp-none">Welcome to TixPesa</p>
        </div>
        <div className="w-full h-1/2  bottom-0 bg-white/20 absolute backdrop-blur-lg/10"/>
      </div>
    </div>
  )
}

export default App
