import * as React from "react"
import Box from "@mui/material/Box"
import Button from "@mui/material/Button"
import FormLabel from "@mui/material/FormLabel"
import FormControl from "@mui/material/FormControl"
import FormGroup from "@mui/material/FormGroup"
import FormControlLabel from "@mui/material/FormControlLabel"
import Checkbox from "@mui/material/Checkbox"
import { Paper } from "@mui/material"
import TextField from "@mui/material/TextField"
import { useEffect, useState } from "react"
import Alert from "@mui/material/Alert"

export default function CheckboxesGroup() {
	const [alert, setAlert] = useState(false)
	const [alertContent, setAlertContent] = useState("")
	const [items, setItems] = React.useState([])
	const [tables, setTables] = React.useState([])
	const [tableID, setTableID] = React.useState("")
	const [checkedState, SetCheckedState] = React.useState([])

	useEffect(() => {
		const abortCont = new AbortController()
		fetch("http://localhost:8000/orders/items", { signal: abortCont.signal })
			.then(res => res.json())
			.then((result) => {
				setItems(result)
				SetCheckedState(new Array(result.length).fill(false))
			})
			.catch(
				err => {
					if (err !== "AbortError") {
						throw err
					}
				}
			)
		return () => abortCont.abort()
	}, [])

	useEffect(() => {
		const abortCont = new AbortController()
		fetch("http://localhost:8000/orders/tables", { signal: abortCont.signal })
			.then(res => res.json())
			.then((result) => {
				setTables(result)
			})
			.catch(
				err => {
					if (err !== "AbortError") {
						throw err
					}
				}
			)
		return () => abortCont.abort()
	}, [])

	const handleChange = (position) => {

		const updateCheckedState = checkedState.map((item, index) =>
			index === position ? !item : item
		)
		SetCheckedState(updateCheckedState)
	}

	const submitOrder = (event) => {
		event.preventDefault()
		let ItemIDs = []
		for (let [idx, isChecked] of checkedState.entries()) {
			if (isChecked) {
				ItemIDs.push(items[idx])
			}
		}
		if (!tables.includes(Number(tableID))) {
			setAlert(true)
			setAlertContent("table id not found")
			return
		}
		fetch(
			`http://localhost:8000/orders/table/${tableID}`,
			{
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify({ item_ids: ItemIDs })
			}
		).then((res) => {
			if (!res.ok) {
				return res.text().then(text => { throw new Error(text) })
			} else {
				setTableID("")
				SetCheckedState((r)=>new Array(r.length).fill(false))
				console.log("insert succeed")
			}
		}).catch(err => {
			setAlert(true)
			setAlertContent(`${err}`)
		})
	}

	const paperStyle = { padding: "30px 100px", margin: "20px auto"}

	return (
		<div>
			{alert ? <Alert severity="error" onClose={() => { setAlert(false) }}>{alertContent}</Alert> : <></>}
			<Box sx={{
				display: "flex",
				alignItems: "center",
				justifyContent: "center",
			}}>
				<Paper elevation={3} style={paperStyle}>
					<FormControl sx={{ m: 10, gap: 5}} component="fieldset" variant="standard">
						<FormLabel sx={{ fontSize: 30}}>Menu</FormLabel>
						<FormGroup>
							{items.map((item, index) => (
								<FormControlLabel key={index}
									control={
										<Checkbox checked={checkedState[index]} onChange={() => handleChange(index)} name={`item-${item}`} />
									}
									label={`item-${item}`}
								/>
							))}
						</FormGroup>
						<TextField
							required
							id="outlined-required"
							label="table number"
							value={tableID}
							onChange={(e) => setTableID(e.target.value)}
						/>
						<Button variant="outlined" onClick={submitOrder}>submit</Button>
					</FormControl>
				</Paper>
			</Box>
		</div>
	)
}
