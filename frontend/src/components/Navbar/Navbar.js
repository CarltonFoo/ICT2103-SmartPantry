import React from "react";
import ReactDOM from 'react-dom';
import { Link } from "react-router-dom";
import Modal from "react-modal";
import { Layout, Menu, Breadcrumb } from "antd";
import {
  UserOutlined,
  ShoppingCartOutlined,
  ShopOutlined,
  OrderedListOutlined,
  AppstoreOutlined
} from '@ant-design/icons';

import "./navbar.css";
import Card from "../Shared/Card";

// submenu keys of first level
const rootSubmenuKeys = ["sub1", "sub2", "sub4"];
const { Header, Content, Sider } = Layout;

const Navbar = (props) => {
  const [openKeys, setOpenKeys] = React.useState(["sub1"]);

  const onOpenChange = (keys) => {
    const latestOpenKey = keys.find((key) => openKeys.indexOf(key) === -1);
    if (rootSubmenuKeys.indexOf(latestOpenKey) === -1) {
      setOpenKeys(keys);
    } else {
      setOpenKeys(latestOpenKey ? [latestOpenKey] : []);
    }
  };

  return (
    <div>
      <Layout class="h-screen">
          <Sider collapsible width={250} class="h-screen" className="fullh">
            <Menu className="logo">
              <Menu.Item key="/" className="logoicon" icon={<ShoppingCartOutlined style={{fontSize: "32px"}}/>} >
                SmartPantry
              </Menu.Item>            
            </Menu>
            <Menu theme="dark" mode="inline" defaultSelectedKeys={['home']} style={{ height: "100%" }}>
              <Menu.Item key="home" icon={<UserOutlined />}>
                Dashboard
                <Link to='/'/>
              </Menu.Item>
              <Menu.Item key="groceries" icon={<ShopOutlined />}>
                Groceries
                <Link to='/groceries'/>
              </Menu.Item>
              <Menu.Item key="recipes" icon={<OrderedListOutlined />}>
                Recipes
                <Link to='/recipes'/>
              </Menu.Item>
              <Menu.Item key="inventory" icon={<AppstoreOutlined />}>
                Inventory
                <Link to='/inventory'/>
              </Menu.Item>
            </Menu>
          </Sider>
          <Layout className="site-layout fullh" >
            <Header className="site-layout-background" style={{ padding: 0 }}>
            </Header>
            <Content>
              <Card>
                {props.children}
              </Card>
            </Content>
          </Layout>
        </Layout>
    </div>
  );
};

export default Navbar;