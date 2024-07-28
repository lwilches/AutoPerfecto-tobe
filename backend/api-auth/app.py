from  src.config.manager_app  import   manager_app , app 
manager_app.init_manager_app( )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)