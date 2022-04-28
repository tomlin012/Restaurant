import './App.css'
import ResponsiveAppBar from './components/appbar'
import CheckboxesGroup from './components/order'
import SearchDataTable from './components/search'
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
						<Route path="/search" element={<SearchDataTable />} />
					</Routes>
				</div>
			</div>
		</Router>
	)
}

export default App
