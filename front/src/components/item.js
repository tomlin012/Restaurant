import * as React from "react"
import { DataGrid } from "@mui/x-data-grid"
import IconButton from "@mui/material/IconButton"
import SearchIcon from "@mui/icons-material/Search"
import TextField from "@mui/material/TextField"
import FormControl from "@mui/material/FormControl"
import { useState } from "react"
import Alert from "@mui/material/Alert"

export default function SearchItem() {
    const [alert, setAlert] = useState(false)
    const [alertContent, setAlertContent] = useState("")
    const [inputQuery, setInputQuery] = useState("")
    const [, setSearchQuery] = useState("")
    const [rows, setRows] = React.useState([])

    const columns = [
        { field: "table_id", headerName: "table id", width: 150 },
        { field: "prepare_time", headerName: "prepare_time( minutes )", width: 150 },
    ]

    const fetchOrder = (event) => {
        event.preventDefault()
        setSearchQuery(inputQuery)
        fetch(`${process.env.REACT_APP_URL}/orders/item/${inputQuery}`)
            .then(res => {
                if (!res.ok) {
                    return res.text().then(text => { throw new Error(text) })
                } else {
                    return res.json()
                }
            })
            .then((result) => { setRows(result) })
            .catch(err => {
                setAlert(true)
                setAlertContent(`${err}`)
            })
    }

    const SearchBar = () => (
        <form>
            <TextField
                id="search-bar"
                className="text"
                value={inputQuery}
                onChange={(e) => {
                    setInputQuery(e.target.value)
                }}
                label="Enter a item id"
                variant="outlined"
                placeholder="Search..."
                size="small"
            />
            <IconButton type="submit" aria-label="search" onClick={fetchOrder}>
                <SearchIcon style={{ fill: "blue" }} />
            </IconButton>
        </form>
    )
    return (
        <div>
            {alert ? <Alert severity="error" onClose={() => { setAlert(false) }}>{alertContent}</Alert> : <></>}
            <FormControl sx={{ gap: 5, mt: 10 }} component="fieldset" variant="standard">
                <SearchBar setSearchQuery={setSearchQuery} />
                <div style={{ height: 400, width: 500 }}>
                    <DataGrid
                        rows={rows}
                        columns={columns}
                    />
                </div>
            </FormControl>
        </div>
    )
}