INCIDENTS = [

    {
        "service": "Payment Database",
        "timestamp": "2026-09-01T10:15:00",
        "incident": "Payment database became unavailable and memory usage reached 96%.",
        "root_cause": "Memory leak after a recent application deployment.",
        "fix": "Rolled back the deployment and restarted the database service.",
        "resolution_time": "18 minutes"
    },

    {
        "service": "Customer Database",
        "timestamp": "2026-09-03T14:20:00",
        "incident": "Database queries became extremely slow and memory usage reached 94%.",
        "root_cause": "Memory leak in a newly deployed database connection component.",
        "fix": "Rolled back the release and restarted affected services.",
        "resolution_time": "22 minutes"
    },

    {
        "service": "Order Database",
        "timestamp": "2026-09-05T09:30:00",
        "incident": "Order processing stopped because the database server ran out of memory.",
        "root_cause": "Unreleased database connections caused continuous memory growth.",
        "fix": "Restarted the service and deployed a connection pool fix.",
        "resolution_time": "31 minutes"
    },

    {
        "service": "Analytics Server",
        "timestamp": "2026-09-07T16:40:00",
        "incident": "Analytics service crashed after memory usage increased above 95%.",
        "root_cause": "Memory leak introduced by a recent analytics deployment.",
        "fix": "Rolled back the deployment and restarted the analytics service.",
        "resolution_time": "25 minutes"
    },

    {
        "service": "Customer Portal",
        "timestamp": "2026-09-02T11:10:00",
        "incident": "Customer portal returned HTTP 500 errors immediately after deployment.",
        "root_cause": "Bad application deployment with incompatible configuration.",
        "fix": "Rolled back the deployment and corrected the configuration.",
        "resolution_time": "15 minutes"
    },

    {
        "service": "Payment Gateway",
        "timestamp": "2026-09-04T13:45:00",
        "incident": "Payment requests started failing after a new release.",
        "root_cause": "Incorrect environment variable introduced during deployment.",
        "fix": "Restored the correct configuration and redeployed the service.",
        "resolution_time": "20 minutes"
    },

    {
        "service": "Authentication API",
        "timestamp": "2026-09-06T08:25:00",
        "incident": "Authentication API returned errors following a production deployment.",
        "root_cause": "Incorrect dependency version in the new deployment.",
        "fix": "Rolled back the release and pinned the compatible dependency version.",
        "resolution_time": "27 minutes"
    },

    {
        "service": "Internal API Gateway",
        "timestamp": "2026-09-08T17:15:00",
        "incident": "API gateway requests failed after the latest production release.",
        "root_cause": "Bad deployment containing an invalid routing configuration.",
        "fix": "Rolled back the deployment and corrected gateway routes.",
        "resolution_time": "19 minutes"
    },

    {
        "service": "User Authentication",
        "timestamp": "2026-09-09T07:50:00",
        "incident": "Users could not log in because the TLS certificate had expired.",
        "root_cause": "Production SSL certificate expired.",
        "fix": "Renewed and installed the certificate and restarted the gateway.",
        "resolution_time": "12 minutes"
    },

    {
        "service": "Public API",
        "timestamp": "2026-09-10T12:30:00",
        "incident": "HTTPS requests failed with certificate validation errors.",
        "root_cause": "Expired TLS certificate on the API endpoint.",
        "fix": "Renewed the certificate and configured automatic certificate renewal.",
        "resolution_time": "14 minutes"
    },

    {
        "service": "Web Server",
        "timestamp": "2026-09-11T15:05:00",
        "incident": "Website became unreachable because HTTPS certificate validation failed.",
        "root_cause": "SSL certificate expired without renewal.",
        "fix": "Installed a new certificate and added expiration monitoring.",
        "resolution_time": "17 minutes"
    },

    {
        "service": "Mobile API",
        "timestamp": "2026-09-12T18:20:00",
        "incident": "Mobile clients could not connect securely to the API.",
        "root_cause": "Expired server certificate.",
        "fix": "Renewed the certificate and verified the complete certificate chain.",
        "resolution_time": "13 minutes"
    },

    {
        "service": "Backup Server",
        "timestamp": "2026-09-13T06:45:00",
        "incident": "Backup jobs failed because the server disk reached 100% usage.",
        "root_cause": "Old backup files and logs consumed available disk space.",
        "fix": "Removed obsolete backups and expanded disk capacity.",
        "resolution_time": "28 minutes"
    },

    {
        "service": "Application Server",
        "timestamp": "2026-09-14T10:50:00",
        "incident": "Application requests failed because the server disk was full.",
        "root_cause": "Application logs grew continuously without rotation.",
        "fix": "Archived old logs, enabled log rotation, and increased storage.",
        "resolution_time": "24 minutes"
    },

    {
        "service": "Inventory Server",
        "timestamp": "2026-09-15T13:35:00",
        "incident": "Inventory updates stopped because disk usage reached 99%.",
        "root_cause": "Temporary files and old logs consumed the filesystem.",
        "fix": "Removed unnecessary files and configured automated cleanup.",
        "resolution_time": "21 minutes"
    },

    {
        "service": "Reporting Server",
        "timestamp": "2026-09-16T19:10:00",
        "incident": "Reports could not be generated because the server filesystem was full.",
        "root_cause": "Large report files were stored indefinitely.",
        "fix": "Deleted old reports and introduced automatic retention policies.",
        "resolution_time": "26 minutes"
    },

    {
        "service": "Product Database",
        "timestamp": "2026-09-17T09:15:00",
        "incident": "Product searches failed because a database index became corrupted.",
        "root_cause": "Corrupted database index after an unexpected database shutdown.",
        "fix": "Rebuilt the affected index and verified database consistency.",
        "resolution_time": "35 minutes"
    },

    {
        "service": "Customer Database",
        "timestamp": "2026-09-18T11:45:00",
        "incident": "Customer queries returned incorrect database errors.",
        "root_cause": "Corrupted index caused query execution failures.",
        "fix": "Rebuilt the affected indexes and ran database integrity checks.",
        "resolution_time": "32 minutes"
    },

    {
        "service": "Order Database",
        "timestamp": "2026-09-19T14:25:00",
        "incident": "Order search queries started failing unexpectedly.",
        "root_cause": "Database index corruption following an unclean shutdown.",
        "fix": "Rebuilt the corrupted index and restored normal query processing.",
        "resolution_time": "29 minutes"
    },

    {
        "service": "Inventory Database",
        "timestamp": "2026-09-20T16:30:00",
        "incident": "Inventory lookup queries failed with database index errors.",
        "root_cause": "Corrupted index on the inventory table.",
        "fix": "Rebuilt the index and performed database consistency validation.",
        "resolution_time": "33 minutes"
    }
]