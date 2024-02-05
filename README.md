# Airflow OAuth Azure AD

This is a simple example of how to use Airflow with OAuth and Azure AD.

```bash
# Create the .env file
cp .env_example .env
```

## Quickstart

Create an Azure AD application and replace the values in the .env file with your own.

**Authentication --> Redirect URI**: `http://localhost:8080/oauth-authorized/azure`

Replace the values in the .env file with your own.

- **Application (client) ID** <--> `AZURE_CLIENT_ID`
- **Directory (tenant) ID** <--> `TENANT_ID`
- **Certificates & secrets -> Client secrets -> Value** <--> `AZURE_CLIENT_SECRET`

If you run on a mac, you need to change the permissions of
the volumes in the docker-compose.yml file

```bash
mkdir -p ./dags ./logs ./plugins
chmod 777 ./dags ./logs ./plugins
```

Start the Airflow webserver

```bash
docker compose up --build -d
```

That's it! You can now access the Airflow webserver at `http://localhost:8080` with your Azure AD credentials.

To add Roles to the users, you need to create Roles in the **App Roles** in the Azure AD application and map using this dictionary in the .env file.

```python
AUTH_ROLES_MAPPING = {
    "AZureAppRoleName": ["RoleInAirflow1", "RoleInAirflow2"],
}
```

To map groups to roles, you need to enter in **Enterprise Application** -> **User and Groups** and map the groups to the App Roles.
