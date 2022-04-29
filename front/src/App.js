import './App.css'
import ResponsiveAppBar from './components/appbar'
import CheckboxesGroup from './components/order'
import SearchTable from './components/table'
import SearchItem from './components/item'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

function App() {
	return (
		<Router>
			<div className="App">
				<ResponsiveAppBar />
				<div className="content">
					<Routes>
						<Route exact path="/" element={<CheckboxesGroup />} />
						<Route path="/order" element={<CheckboxesGroup />} />
						<Route path="/table" element={<SearchTable />} />
						<Route path="/item" element={<SearchItem />} />
					</Routes>
				</div>
			</div>
		</Router>
	)
}

export default App
