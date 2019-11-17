/*for normal tables */
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE auth_group to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE auth_group_permissions to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE auth_permission to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE auth_user to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE auth_user_groups to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE auth_user_user_permissions to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE django_admin_log to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE django_content_type to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE django_migrations to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE django_session to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE mart_order to demo_user;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON TABLE mart_product to demo_user;

GRANT SELECT ON TABLE auth_group to demo_readonly;
GRANT SELECT ON TABLE auth_group_permissions to demo_readonly;
GRANT SELECT ON TABLE auth_permission to demo_readonly;
GRANT SELECT ON TABLE auth_user to demo_readonly;
GRANT SELECT ON TABLE auth_user_groups to demo_readonly;
GRANT SELECT ON TABLE auth_user_user_permissions to demo_readonly;
GRANT SELECT ON TABLE django_admin_log to demo_readonly;
GRANT SELECT ON TABLE django_content_type to demo_readonly;
GRANT SELECT ON TABLE django_migrations to demo_readonly;
GRANT SELECT ON TABLE django_session to demo_readonly;
GRANT SELECT ON TABLE mart_order to demo_readonly;
GRANT SELECT ON TABLE mart_product to demo_readonly;
