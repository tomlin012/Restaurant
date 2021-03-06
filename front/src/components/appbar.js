import * as React from "react"
import AppBar from "@mui/material/AppBar"
import Box from "@mui/material/Box"
import Toolbar from "@mui/material/Toolbar"
import IconButton from "@mui/material/IconButton"
import Typography from "@mui/material/Typography"
import MenuIcon from "@mui/icons-material/Menu"
import Container from "@mui/material/Container"
import Button from "@mui/material/Button"
import RestaurantIcon from "@mui/icons-material/Restaurant"
import { Link } from "react-router-dom"

export default function ResponsiveAppBar() {

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Typography
            variant="h6"
            noWrap
            component="div"
            sx={{ mr: 2, display: { xs: "none", md: "flex" } }}
          >
            <RestaurantIcon />
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
          </Box>
          <Typography
            variant="h6"
            noWrap
            component="div"
            sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}
          >
            LOGO
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
            <Button
              key="order"
              component={Link} to={`/order`}
              sx={{ my: 2, color: "white", display: "block" }}
            >
              order
            </Button>
            <Button
              key="table"
              component={Link} to={`/table`}
              sx={{ my: 2, color: "white", display: "block" }}
            >
              table
            </Button>
            <Button
              key="item"
              component={Link} to={`/item`}
              sx={{ my: 2, color: "white", display: "block" }}
            >
              item
            </Button>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  )
}
