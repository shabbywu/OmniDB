from fastapi import Depends
from OmniDB_app.views.fastapi import app, dependencies


@app.post("/get_tree_info_postgresql/")
def get_tree_info(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    try:
        v_return["v_data"] = {
            "v_mode": "database",
            "v_database_return": {
                "v_database": v_database.GetName(),
                "version": v_database.GetVersion(),
                #'superuser': v_database.GetUserSuper(),
                "create_role": v_database.TemplateCreateRole().v_text,
                "alter_role": v_database.TemplateAlterRole().v_text,
                "drop_role": v_database.TemplateDropRole().v_text,
                "create_tablespace": v_database.TemplateCreateTablespace().v_text,
                "alter_tablespace": v_database.TemplateAlterTablespace().v_text,
                "drop_tablespace": v_database.TemplateDropTablespace().v_text,
                "create_database": v_database.TemplateCreateDatabase().v_text,
                "alter_database": v_database.TemplateAlterDatabase().v_text,
                "drop_database": v_database.TemplateDropDatabase().v_text,
                "create_extension": v_database.TemplateCreateExtension().v_text,
                "alter_extension": v_database.TemplateAlterExtension().v_text,
                "drop_extension": v_database.TemplateDropExtension().v_text,
                "create_schema": v_database.TemplateCreateSchema().v_text,
                "alter_schema": v_database.TemplateAlterSchema().v_text,
                "drop_schema": v_database.TemplateDropSchema().v_text,
                "create_sequence": v_database.TemplateCreateSequence().v_text,
                "alter_sequence": v_database.TemplateAlterSequence().v_text,
                "drop_sequence": v_database.TemplateDropSequence().v_text,
                "create_function": v_database.TemplateCreateFunction().v_text,
                "alter_function": v_database.TemplateAlterFunction().v_text,
                "drop_function": v_database.TemplateDropFunction().v_text,
                "create_procedure": v_database.TemplateCreateProcedure().v_text,
                "alter_procedure": v_database.TemplateAlterProcedure().v_text,
                "drop_procedure": v_database.TemplateDropProcedure().v_text,
                "create_triggerfunction": v_database.TemplateCreateTriggerFunction().v_text,
                "alter_triggerfunction": v_database.TemplateAlterTriggerFunction().v_text,
                "drop_triggerfunction": v_database.TemplateDropTriggerFunction().v_text,
                "create_eventtriggerfunction": v_database.TemplateCreateEventTriggerFunction().v_text,
                "alter_eventtriggerfunction": v_database.TemplateAlterEventTriggerFunction().v_text,
                "drop_eventtriggerfunction": v_database.TemplateDropEventTriggerFunction().v_text,
                "create_aggregate": v_database.TemplateCreateAggregate().v_text,
                "alter_aggregate": v_database.TemplateAlterAggregate().v_text,
                "drop_aggregate": v_database.TemplateDropAggregate().v_text,
                "create_view": v_database.TemplateCreateView().v_text,
                "alter_view": v_database.TemplateAlterView().v_text,
                "drop_view": v_database.TemplateDropView().v_text,
                "create_mview": v_database.TemplateCreateMaterializedView().v_text,
                "refresh_mview": v_database.TemplateRefreshMaterializedView().v_text,
                "alter_mview": v_database.TemplateAlterMaterializedView().v_text,
                "drop_mview": v_database.TemplateDropMaterializedView().v_text,
                "create_table": v_database.TemplateCreateTable().v_text,
                "alter_table": v_database.TemplateAlterTable().v_text,
                "drop_table": v_database.TemplateDropTable().v_text,
                "create_column": v_database.TemplateCreateColumn().v_text,
                "alter_column": v_database.TemplateAlterColumn().v_text,
                "drop_column": v_database.TemplateDropColumn().v_text,
                "create_primarykey": v_database.TemplateCreatePrimaryKey().v_text,
                "drop_primarykey": v_database.TemplateDropPrimaryKey().v_text,
                "create_unique": v_database.TemplateCreateUnique().v_text,
                "drop_unique": v_database.TemplateDropUnique().v_text,
                "create_foreignkey": v_database.TemplateCreateForeignKey().v_text,
                "drop_foreignkey": v_database.TemplateDropForeignKey().v_text,
                "create_index": v_database.TemplateCreateIndex().v_text,
                "alter_index": v_database.TemplateAlterIndex().v_text,
                "cluster_index": v_database.TemplateClusterIndex().v_text,
                "reindex": v_database.TemplateReindex().v_text,
                "drop_index": v_database.TemplateDropIndex().v_text,
                "create_check": v_database.TemplateCreateCheck().v_text,
                "drop_check": v_database.TemplateDropCheck().v_text,
                "create_exclude": v_database.TemplateCreateExclude().v_text,
                "drop_exclude": v_database.TemplateDropExclude().v_text,
                "create_rule": v_database.TemplateCreateRule().v_text,
                "alter_rule": v_database.TemplateAlterRule().v_text,
                "drop_rule": v_database.TemplateDropRule().v_text,
                "create_trigger": v_database.TemplateCreateTrigger().v_text,
                "create_view_trigger": v_database.TemplateCreateViewTrigger().v_text,
                "alter_trigger": v_database.TemplateAlterTrigger().v_text,
                "enable_trigger": v_database.TemplateEnableTrigger().v_text,
                "disable_trigger": v_database.TemplateDisableTrigger().v_text,
                "drop_trigger": v_database.TemplateDropTrigger().v_text,
                "create_eventtrigger": v_database.TemplateCreateEventTrigger().v_text,
                "alter_eventtrigger": v_database.TemplateAlterEventTrigger().v_text,
                "enable_eventtrigger": v_database.TemplateEnableEventTrigger().v_text,
                "disable_eventtrigger": v_database.TemplateDisableEventTrigger().v_text,
                "drop_eventtrigger": v_database.TemplateDropEventTrigger().v_text,
                "create_inherited": v_database.TemplateCreateInherited().v_text,
                "noinherit_partition": v_database.TemplateNoInheritPartition().v_text,
                "create_partition": v_database.TemplateCreatePartition().v_text,
                "detach_partition": v_database.TemplateDetachPartition().v_text,
                "drop_partition": v_database.TemplateDropPartition().v_text,
                "vacuum": v_database.TemplateVacuum().v_text,
                "vacuum_table": v_database.TemplateVacuumTable().v_text,
                "analyze": v_database.TemplateAnalyze().v_text,
                "analyze_table": v_database.TemplateAnalyzeTable().v_text,
                "delete": v_database.TemplateDelete().v_text,
                "truncate": v_database.TemplateTruncate().v_text,
                "create_physicalreplicationslot": v_database.TemplateCreatePhysicalReplicationSlot().v_text,
                "drop_physicalreplicationslot": v_database.TemplateDropPhysicalReplicationSlot().v_text,
                "create_logicalreplicationslot": v_database.TemplateCreateLogicalReplicationSlot().v_text,
                "drop_logicalreplicationslot": v_database.TemplateDropLogicalReplicationSlot().v_text,
                "create_publication": v_database.TemplateCreatePublication().v_text,
                "alter_publication": v_database.TemplateAlterPublication().v_text,
                "drop_publication": v_database.TemplateDropPublication().v_text,
                "add_pubtable": v_database.TemplateAddPublicationTable().v_text,
                "drop_pubtable": v_database.TemplateDropPublicationTable().v_text,
                "create_subscription": v_database.TemplateCreateSubscription().v_text,
                "alter_subscription": v_database.TemplateAlterSubscription().v_text,
                "drop_subscription": v_database.TemplateDropSubscription().v_text,
                "create_fdw": v_database.TemplateCreateForeignDataWrapper().v_text,
                "alter_fdw": v_database.TemplateAlterForeignDataWrapper().v_text,
                "drop_fdw": v_database.TemplateDropForeignDataWrapper().v_text,
                "create_foreign_server": v_database.TemplateCreateForeignServer().v_text,
                "alter_foreign_server": v_database.TemplateAlterForeignServer().v_text,
                "import_foreign_schema": v_database.TemplateImportForeignSchema().v_text,
                "drop_foreign_server": v_database.TemplateDropForeignServer().v_text,
                "create_foreign_table": v_database.TemplateCreateForeignTable().v_text,
                "alter_foreign_table": v_database.TemplateAlterForeignTable().v_text,
                "drop_foreign_table": v_database.TemplateDropForeignTable().v_text,
                "create_foreign_column": v_database.TemplateCreateForeignColumn().v_text,
                "alter_foreign_column": v_database.TemplateAlterForeignColumn().v_text,
                "drop_foreign_column": v_database.TemplateDropForeignColumn().v_text,
                "create_user_mapping": v_database.TemplateCreateUserMapping().v_text,
                "alter_user_mapping": v_database.TemplateAlterUserMapping().v_text,
                "drop_user_mapping": v_database.TemplateDropUserMapping().v_text,
                "create_type": v_database.TemplateCreateType().v_text,
                "alter_type": v_database.TemplateAlterType().v_text,
                "drop_type": v_database.TemplateDropType().v_text,
                "create_domain": v_database.TemplateCreateDomain().v_text,
                "alter_domain": v_database.TemplateAlterDomain().v_text,
                "drop_domain": v_database.TemplateDropDomain().v_text,
                "create_statistics": v_database.TemplateCreateStatistics().v_text,
                "alter_statistics": v_database.TemplateAlterStatistics().v_text,
                "drop_statistics": v_database.TemplateDropStatistics().v_text,
            },
        }
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_database_objects_postgresql/")
def get_database_objects(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    try:
        v_return["v_data"] = {}
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_properties_postgresql/")
def get_properties(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_data = json_object["p_data"]

    v_list_properties = []
    v_ddl = ""

    try:
        v_properties = v_database.GetProperties(
            v_data["p_schema"], v_data["p_table"], v_data["p_object"], v_data["p_type"]
        )
        for v_property in v_properties.Rows:
            v_list_properties.append([v_property["Property"], v_property["Value"]])
        v_ddl = v_database.GetDDL(
            v_data["p_schema"], v_data["p_table"], v_data["p_object"], v_data["p_type"]
        )
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = {"properties": v_list_properties, "ddl": v_ddl}

    return v_return


@app.post("/get_tables_postgresql/")
def get_tables(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryTables(False, v_schema)
        for v_table in v_tables.Rows:
            v_table_data = {
                "v_name": v_table["table_name"],
                "v_has_primary_keys": v_database.v_has_primary_keys,
                "v_has_foreign_keys": v_database.v_has_foreign_keys,
                "v_has_uniques": v_database.v_has_uniques,
                "v_has_indexes": v_database.v_has_indexes,
                "v_has_checks": v_database.v_has_checks,
                "v_has_excludes": v_database.v_has_excludes,
                "v_has_rules": v_database.v_has_rules,
                "v_has_triggers": v_database.v_has_triggers,
                "v_has_partitions": v_database.v_has_partitions,
                "v_has_statistics": v_database.v_has_statistics,
                "v_oid": v_table["oid"],
            }
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_columns_postgresql/")
def get_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_columns = []

    try:
        v_columns = v_database.QueryTablesFields(v_table, False, v_schema)
        for v_column in v_columns.Rows:
            v_column_data = {
                "v_column_name": v_column["column_name"],
                "v_data_type": v_column["data_type"],
                "v_data_length": v_column["data_length"],
                "v_nullable": v_column["nullable"],
                "v_position": v_column["position"],
            }
            v_list_columns.append(v_column_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_columns

    return v_return


@app.post("/get_pk_postgresql/")
def get_pk(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_pk = []

    try:
        v_pks = v_database.QueryTablesPrimaryKeys(v_table, False, v_schema)
        for v_pk in v_pks.Rows:
            v_pk_data = []
            v_pk_data.append(v_pk["constraint_name"])
            v_pk_data.append(v_pk["oid"])
            v_list_pk.append(v_pk_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_pk

    return v_return


@app.post("/get_pk_columns_postgresql/")
def get_pk_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_pkey = json_object["p_key"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_pk = []

    try:
        v_pks = v_database.QueryTablesPrimaryKeysColumns(
            v_pkey, v_table, False, v_schema
        )
        for v_pk in v_pks.Rows:
            v_pk_data = []
            v_pk_data.append(v_pk["column_name"])
            v_list_pk.append(v_pk_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_pk

    return v_return


@app.post("/get_fks_postgresql/")
def get_fks(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_fk = []

    try:
        v_fks = v_database.QueryTablesForeignKeys(v_table, False, v_schema)
        for v_fk in v_fks.Rows:
            v_fk_data = []
            v_fk_data.append(v_fk["constraint_name"])
            v_fk_data.append(v_fk["r_table_name"])
            v_fk_data.append(v_fk["delete_rule"])
            v_fk_data.append(v_fk["update_rule"])
            v_fk_data.append(v_fk["oid"])
            v_list_fk.append(v_fk_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_fk

    return v_return


@app.post("/get_fks_columns_postgresql/")
def get_fks_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_fkey = json_object["p_fkey"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_fk = []

    try:
        v_fks = v_database.QueryTablesForeignKeysColumns(
            v_fkey, v_table, False, v_schema
        )
        for v_fk in v_fks.Rows:
            v_fk_data = []
            v_fk_data.append(v_fk["r_table_name"])
            v_fk_data.append(v_fk["delete_rule"])
            v_fk_data.append(v_fk["update_rule"])
            v_fk_data.append(v_fk["column_name"])
            v_fk_data.append(v_fk["r_column_name"])
            v_list_fk.append(v_fk_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_fk

    return v_return


@app.post("/get_uniques_postgresql/")
def get_uniques(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_uniques = []

    try:
        v_uniques = v_database.QueryTablesUniques(v_table, False, v_schema)
        for v_unique in v_uniques.Rows:
            v_unique_data = []
            v_unique_data.append(v_unique["constraint_name"])
            v_unique_data.append(v_unique["oid"])
            v_list_uniques.append(v_unique_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_uniques

    return v_return


@app.post("/get_uniques_columns_postgresql/")
def get_uniques_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_unique = json_object["p_unique"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_uniques = []

    try:
        v_uniques = v_database.QueryTablesUniquesColumns(
            v_unique, v_table, False, v_schema
        )
        for v_unique in v_uniques.Rows:
            v_unique_data = []
            v_unique_data.append(v_unique["column_name"])
            v_list_uniques.append(v_unique_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_uniques

    return v_return


@app.post("/get_indexes_postgresql/")
def get_indexes(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_indexes = []

    try:
        v_indexes = v_database.QueryTablesIndexes(v_table, False, v_schema)
        for v_index in v_indexes.Rows:
            v_index_data = []
            v_index_data.append(v_index["index_name"])
            v_index_data.append(v_index["uniqueness"])
            v_index_data.append(v_index["oid"])
            v_list_indexes.append(v_index_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_indexes

    return v_return


@app.post("/get_indexes_columns_postgresql/")
def get_indexes_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_index = json_object["p_index"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_indexes = []

    try:
        v_indexes = v_database.QueryTablesIndexesColumns(
            v_index, v_table, False, v_schema
        )
        for v_index in v_indexes.Rows:
            v_index_data = []
            v_index_data.append(v_index["column_name"])
            v_list_indexes.append(v_index_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_indexes

    return v_return


@app.post("/get_checks_postgresql/")
def get_checks(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_checks = []

    try:
        v_checks = v_database.QueryTablesChecks(v_table, False, v_schema)
        for v_check in v_checks.Rows:
            v_check_data = []
            v_check_data.append(v_check["constraint_name"])
            v_check_data.append(v_check["constraint_source"])
            v_check_data.append(v_check["oid"])
            v_list_checks.append(v_check_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_checks

    return v_return


@app.post("/get_excludes_postgresql/")
def get_excludes(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_excludes = []

    try:
        v_excludes = v_database.QueryTablesExcludes(v_table, False, v_schema)
        for v_exclude in v_excludes.Rows:
            v_exclude_data = []
            v_exclude_data.append(v_exclude["constraint_name"])
            v_exclude_data.append(v_exclude["attributes"])
            v_exclude_data.append(v_exclude["operations"])
            v_exclude_data.append(v_exclude["oid"])
            v_list_excludes.append(v_exclude_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_excludes

    return v_return


@app.post("/get_rules_postgresql/")
def get_rules(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_rules = []

    try:
        v_rules = v_database.QueryTablesRules(v_table, False, v_schema)
        for v_rule in v_rules.Rows:
            v_rule_data = []
            v_rule_data.append(v_rule["rule_name"])
            v_rule_data.append(v_rule["oid"])
            v_list_rules.append(v_rule_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_rules

    return v_return


@app.post("/get_rule_definition_postgresql/")
def get_rule_definition(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_rule = json_object["p_rule"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    try:
        v_return["v_data"] = v_database.GetRuleDefinition(v_rule, v_table, v_schema)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_triggers_postgresql/")
def get_triggers(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_triggers = []

    try:
        v_triggers = v_database.QueryTablesTriggers(v_table, False, v_schema)
        for v_trigger in v_triggers.Rows:
            v_trigger_data = {
                "v_name": v_trigger["trigger_name"],
                "v_enabled": v_trigger["trigger_enabled"],
                "v_function": v_trigger["trigger_function"],
                "v_id": v_trigger["id"],
                "v_function_oid": v_trigger["function_oid"],
                "v_oid": v_trigger["oid"],
            }
            v_list_triggers.append(v_trigger_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_triggers

    return v_return


@app.post("/get_eventtriggers_postgresql/")
def get_eventtriggers(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_triggers = []

    try:
        v_triggers = v_database.QueryEventTriggers()
        for v_trigger in v_triggers.Rows:
            v_trigger_data = {
                "v_name": v_trigger["trigger_name"],
                "v_enabled": v_trigger["trigger_enabled"],
                "v_event": v_trigger["event_name"],
                "v_function": v_trigger["trigger_function"],
                "v_id": v_trigger["id"],
                "v_function_oid": v_trigger["function_oid"],
                "v_oid": v_trigger["oid"],
            }
            v_list_triggers.append(v_trigger_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_triggers

    return v_return


@app.post("/get_inheriteds_postgresql/")
def get_inheriteds(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_partitions = []

    try:
        v_partitions = v_database.QueryTablesInheriteds(v_table, False, v_schema)
        for v_partition in v_partitions.Rows:
            v_partition_data = []
            v_partition_data.append(
                v_partition["child_schema"] + "." + v_partition["child_table"]
            )
            v_list_partitions.append(v_partition_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_partitions

    return v_return


@app.post("/get_partitions_postgresql/")
def get_partitions(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):
    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_partitions = []

    try:
        v_partitions = v_database.QueryTablesPartitions(v_table, False, v_schema)
        for v_partition in v_partitions.Rows:
            v_partition_data = []
            v_partition_data.append(
                v_partition["child_schema"] + "." + v_partition["child_table"]
            )
            v_list_partitions.append(v_partition_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_partitions

    return v_return


@app.post("/get_statistics_postgresql/")
def get_statistics(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_statistics = []

    try:
        v_statistics = v_database.QueryTablesStatistics(v_table, False, v_schema)
        for v_statistic in v_statistics.Rows:
            v_statistic_data = []
            v_statistic_data.append(v_statistic["statistic_name"])
            v_statistic_data.append(v_statistic["schema_name"])
            v_statistic_data.append(v_statistic["oid"])
            v_list_statistics.append(v_statistic_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_statistics

    return v_return


@app.post("/get_statistics_columns_postgresql/")
def get_statistics_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_statistics = json_object["p_statistics"]
    v_schema = json_object["p_schema"]

    v_list_columns = []

    try:
        v_columns = v_database.QueryStatisticsFields(v_statistics, False, v_schema)
        for v_column in v_columns.Rows:
            v_column_data = {"v_column_name": v_column["column_name"]}
            v_list_columns.append(v_column_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_columns

    return v_return


@app.post("/get_views_postgresql/")
def get_views(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryViews(False, v_schema)
        for v_table in v_tables.Rows:
            v_table_data = {
                "v_name": v_table["table_name"],
                "v_has_rules": v_database.v_has_rules,
                "v_has_triggers": v_database.v_has_triggers,
                "v_oid": v_table["oid"],
            }
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_views_columns_postgresql/")
def get_views_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_columns = []

    try:
        v_columns = v_database.QueryViewFields(v_table, False, v_schema)
        for v_column in v_columns.Rows:
            v_column_data = {
                "v_column_name": v_column["column_name"],
                "v_data_type": v_column["data_type"],
                "v_data_length": v_column["data_length"],
            }
            v_list_columns.append(v_column_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_columns

    return v_return


@app.post("/get_view_definition_postgresql/")
def get_view_definition(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_view = json_object["p_view"]
    v_schema = json_object["p_schema"]

    try:
        v_return["v_data"] = v_database.GetViewDefinition(v_view, v_schema)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_mviews_postgresql/")
def get_mviews(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryMaterializedViews(False, v_schema)
        for v_table in v_tables.Rows:
            v_table_data = {
                "v_name": v_table["table_name"],
                "v_has_indexes": v_database.v_has_indexes,
                "v_has_statistics": v_database.v_has_statistics,
                "v_oid": v_table["oid"],
            }
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_mviews_columns_postgresql/")
def get_mviews_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_columns = []

    try:
        v_columns = v_database.QueryMaterializedViewFields(v_table, False, v_schema)
        for v_column in v_columns.Rows:
            v_column_data = {
                "v_column_name": v_column["column_name"],
                "v_data_type": v_column["data_type"],
                "v_data_length": v_column["data_length"],
            }
            v_list_columns.append(v_column_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_columns

    return v_return


@app.post("/get_mview_definition_postgresql/")
def get_mview_definition(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_view = json_object["p_view"]
    v_schema = json_object["p_schema"]

    try:
        v_return["v_data"] = v_database.GetMaterializedViewDefinition(v_view, v_schema)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_schemas_postgresql/")
def get_schemas(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_schemas = []

    try:
        v_schemas = v_database.QuerySchemas()
        for v_schema in v_schemas.Rows:
            v_schema_data = {
                "v_name": v_schema["schema_name"],
                "v_oid": v_schema["oid"],
            }
            v_list_schemas.append(v_schema_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_schemas

    return v_return


@app.post("/get_databases_postgresql/")
def get_databases(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_databases = []

    try:
        v_databases = v_database.QueryDatabases()
        for v_database in v_databases.Rows:
            v_database_data = {
                "v_name": v_database["database_name"],
                "v_oid": v_database["oid"],
            }
            v_list_databases.append(v_database_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_databases

    return v_return


@app.post("/get_tablespaces_postgresql/")
def get_tablespaces(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_tablespaces = []

    try:
        v_tablespaces = v_database.QueryTablespaces()
        for v_tablespace in v_tablespaces.Rows:
            v_tablespace_data = {
                "v_name": v_tablespace["tablespace_name"],
                "v_oid": v_tablespace["oid"],
            }
            v_list_tablespaces.append(v_tablespace_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tablespaces

    return v_return


@app.post("/get_roles_postgresql/")
def get_roles(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_roles = []

    try:
        v_roles = v_database.QueryRoles()
        for v_role in v_roles.Rows:
            v_role_data = {"v_name": v_role["role_name"], "v_oid": v_role["oid"]}
            v_list_roles.append(v_role_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_roles

    return v_return


@app.post("/get_functions_postgresql/")
def get_functions(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_functions = []

    try:
        v_functions = v_database.QueryFunctions(False, v_schema)
        for v_function in v_functions.Rows:
            v_function_data = {
                "v_name": v_function["name"],
                "v_id": v_function["id"],
                "v_function_oid": v_function["function_oid"],
            }
            v_list_functions.append(v_function_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_functions

    return v_return


@app.post("/get_function_fields_postgresql/")
def get_function_fields(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_function"]
    v_schema = json_object["p_schema"]

    v_list_fields = []

    try:
        v_fields = v_database.QueryFunctionFields(v_function, v_schema)
        for v_field in v_fields.Rows:
            v_field_data = {"v_name": v_field["name"], "v_type": v_field["type"]}
            v_list_fields.append(v_field_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_fields

    return v_return


@app.post("/get_function_definition_postgresql/")
def get_function_definition(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_function"]

    try:
        v_return["v_data"] = v_database.GetFunctionDefinition(v_function)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_function_debug_postgresql/")
def get_function_debug(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_function"]

    try:
        v_return["v_data"] = v_database.GetFunctionDebug(v_function)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_procedures_postgresql/")
def get_procedures(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_functions = []

    try:
        v_functions = v_database.QueryProcedures(False, v_schema)
        for v_function in v_functions.Rows:
            v_function_data = {
                "v_name": v_function["name"],
                "v_id": v_function["id"],
                "v_function_oid": v_function["function_oid"],
            }
            v_list_functions.append(v_function_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_functions

    return v_return


@app.post("/get_procedure_fields_postgresql/")
def get_procedure_fields(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_procedure"]
    v_schema = json_object["p_schema"]

    v_list_fields = []

    try:
        v_fields = v_database.QueryProcedureFields(v_function, v_schema)
        for v_field in v_fields.Rows:
            v_field_data = {"v_name": v_field["name"], "v_type": v_field["type"]}
            v_list_fields.append(v_field_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_fields

    return v_return


@app.post("/get_procedure_definition_postgresql/")
def get_procedure_definition(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_procedure"]

    try:
        v_return["v_data"] = v_database.GetProcedureDefinition(v_function)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_procedure_debug_postgresql/")
def get_procedure_debug(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_procedure"]

    try:
        v_return["v_data"] = v_database.GetProcedureDebug(v_function)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_triggerfunctions_postgresql/")
def get_triggerfunctions(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_functions = []

    try:
        v_functions = v_database.QueryTriggerFunctions(False, v_schema)
        for v_function in v_functions.Rows:
            v_function_data = {
                "v_name": v_function["name"],
                "v_id": v_function["id"],
                "v_function_oid": v_function["function_oid"],
            }
            v_list_functions.append(v_function_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_functions

    return v_return


@app.post("/get_triggerfunction_definition_postgresql/")
def get_triggerfunction_definition(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_function"]

    try:
        v_return["v_data"] = v_database.GetTriggerFunctionDefinition(v_function)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_eventtriggerfunctions_postgresql/")
def get_eventtriggerfunctions(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_functions = []

    try:
        v_functions = v_database.QueryEventTriggerFunctions(False, v_schema)
        for v_function in v_functions.Rows:
            v_function_data = {
                "v_name": v_function["name"],
                "v_id": v_function["id"],
                "v_function_oid": v_function["function_oid"],
            }
            v_list_functions.append(v_function_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_functions

    return v_return


@app.post("/get_eventtriggerfunction_definition_postgresql/")
def get_eventtriggerfunction_definition(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_function"]

    try:
        v_return["v_data"] = v_database.GetEventTriggerFunctionDefinition(v_function)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_aggregates_postgresql/")
def get_aggregates(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_aggregates = []

    try:
        v_aggregates = v_database.QueryAggregates(False, v_schema)
        for v_aggregate in v_aggregates.Rows:
            v_aggregate_data = {
                "v_name": v_aggregate["name"],
                "v_id": v_aggregate["id"],
                "v_oid": v_aggregate["oid"],
            }
            v_list_aggregates.append(v_aggregate_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_aggregates

    return v_return


@app.post("/get_sequences_postgresql/")
def get_sequences(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_sequences = []

    try:
        v_sequences = v_database.QuerySequences(False, v_schema)
        for v_sequence in v_sequences.Rows:
            v_sequence_data = {
                "v_sequence_name": v_sequence["sequence_name"],
                "v_oid": v_sequence["oid"],
            }
            v_list_sequences.append(v_sequence_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_sequences

    return v_return


@app.post("/get_extensions_postgresql/")
def get_extensions(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_extensions = []

    try:
        v_extensions = v_database.QueryExtensions()
        for v_extension in v_extensions.Rows:
            v_extension_data = {
                "v_name": v_extension["extension_name"],
                "v_oid": v_extension["oid"],
            }
            v_list_extensions.append(v_extension_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_extensions

    return v_return


@app.post("/get_physicalreplicationslots_postgresql/")
def get_physicalreplicationslots(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_repslots = []

    try:
        v_repslots = v_database.QueryPhysicalReplicationSlots()
        for v_repslot in v_repslots.Rows:
            v_repslot_data = {"v_name": v_repslot["slot_name"]}
            v_list_repslots.append(v_repslot_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_repslots

    return v_return


@app.post("/get_logicalreplicationslots_postgresql/")
def get_logicalreplicationslots(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_repslots = []

    try:
        v_repslots = v_database.QueryLogicalReplicationSlots()
        for v_repslot in v_repslots.Rows:
            v_repslot_data = {"v_name": v_repslot["slot_name"]}
            v_list_repslots.append(v_repslot_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_repslots

    return v_return


@app.post("/get_publications_postgresql/")
def get_publications(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_pubs = []

    try:
        v_pubs = v_database.QueryPublications()
        for v_pub in v_pubs.Rows:
            v_pub_data = {
                "v_name": v_pub["pubname"],
                "v_alltables": v_pub["puballtables"],
                "v_insert": v_pub["pubinsert"],
                "v_update": v_pub["pubupdate"],
                "v_delete": v_pub["pubdelete"],
                "v_truncate": v_pub["pubtruncate"],
                "v_oid": v_pub["oid"],
            }
            v_list_pubs.append(v_pub_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_pubs

    return v_return


@app.post("/get_publication_tables_postgresql/")
def get_publication_tables(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_pub = json_object["p_pub"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryPublicationTables(v_pub)
        for v_table in v_tables.Rows:
            v_table_data = {"v_name": v_table["table_name"]}
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_subscriptions_postgresql/")
def get_subscriptions(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_subs = []

    try:
        v_subs = v_database.QuerySubscriptions()
        for v_sub in v_subs.Rows:
            v_sub_data = {
                "v_name": v_sub["subname"],
                "v_enabled": v_sub["subenabled"],
                "v_conninfo": v_sub["subconninfo"],
                "v_publications": v_sub["subpublications"],
                "v_oid": v_sub["oid"],
            }
            v_list_subs.append(v_sub_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_subs

    return v_return


@app.post("/get_subscription_tables_postgresql/")
def get_subscription_tables(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_sub = json_object["p_sub"]

    v_list_tables = []

    try:
        v_tables = v_database.QuerySubscriptionTables(v_sub)
        for v_table in v_tables.Rows:
            v_table_data = {"v_name": v_table["table_name"]}
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_foreign_data_wrappers_postgresql/")
def get_foreign_data_wrappers(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    v_list_fdws = []

    try:
        v_fdws = v_database.QueryForeignDataWrappers()
        for v_fdw in v_fdws.Rows:
            v_fdw_data = {"v_name": v_fdw["fdwname"], "v_oid": v_fdw["oid"]}
            v_list_fdws.append(v_fdw_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_fdws

    return v_return


@app.post("/get_foreign_servers_postgresql/")
def get_foreign_servers(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_fdw = json_object["p_fdw"]

    v_list_servers = []

    try:
        v_servers = v_database.QueryForeignServers(v_fdw)
        for v_server in v_servers.Rows:
            v_server_data = {
                "v_name": v_server["srvname"],
                "v_type": v_server["srvtype"],
                "v_version": v_server["srvversion"],
                "v_options": v_server["srvoptions"],
                "v_oid": v_server["oid"],
            }
            v_list_servers.append(v_server_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_servers

    return v_return


@app.post("/get_user_mappings_postgresql/")
def get_user_mappings(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_foreign_server = json_object["p_foreign_server"]

    v_list_mappings = []

    try:
        v_mappings = v_database.QueryUserMappings(v_foreign_server)
        for v_mapping in v_mappings.Rows:
            v_mapping_data = {
                "v_name": v_mapping["rolname"],
                "v_options": v_mapping["umoptions"],
                "v_foreign_server": v_foreign_server,
            }
            v_list_mappings.append(v_mapping_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_mappings

    return v_return


@app.post("/get_foreign_tables_postgresql/")
def get_foreign_tables(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryForeignTables(False, v_schema)
        for v_table in v_tables.Rows:
            v_table_data = {
                "v_name": v_table["table_name"],
                "v_has_statistics": v_database.v_has_statistics,
                "v_oid": v_table["oid"],
            }
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_foreign_columns_postgresql/")
def get_foreign_columns(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_columns = []

    try:
        v_columns = v_database.QueryForeignTablesFields(v_table, False, v_schema)
        for v_column in v_columns.Rows:
            v_column_data = {
                "v_column_name": v_column["column_name"],
                "v_data_type": v_column["data_type"],
                "v_data_length": v_column["data_length"],
                "v_nullable": v_column["nullable"],
                "v_options": v_column["attfdwoptions"],
                "v_tableoptions": v_column["ftoptions"],
                "v_server": v_column["srvname"],
                "v_fdw": v_column["fdwname"],
            }
            v_list_columns.append(v_column_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_columns

    return v_return


@app.post("/get_types_postgresql/")
def get_types(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_types = []

    try:
        v_types = v_database.QueryTypes(False, v_schema)
        for v_type in v_types.Rows:
            v_type_data = {"v_type_name": v_type["type_name"], "v_oid": v_type["oid"]}
            v_list_types.append(v_type_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_types

    return v_return


@app.post("/get_domains_postgresql/")
def get_domains(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_domains = []

    try:
        v_domains = v_database.QueryDomains(False, v_schema)
        for v_domain in v_domains.Rows:
            v_domain_data = {
                "v_domain_name": v_domain["domain_name"],
                "v_oid": v_domain["oid"],
            }
            v_list_domains.append(v_domain_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_domains

    return v_return


@app.post("/get_inheriteds_parents_postgresql/")
def get_inheriteds_parents(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryTablesInheritedsParents(False, v_schema)
        for v_table in v_tables.Rows:
            v_table_data = {
                "v_name": v_table["table_schema"] + "." + v_table["table_name"]
            }
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_inheriteds_children_postgresql/")
def get_inheriteds_children(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryTablesInheritedsChildren(v_table, v_schema)
        for v_table in v_tables.Rows:
            v_table_data = {
                "v_name": v_table["table_name"],
                "v_has_primary_keys": v_database.v_has_primary_keys,
                "v_has_foreign_keys": v_database.v_has_foreign_keys,
                "v_has_uniques": v_database.v_has_uniques,
                "v_has_indexes": v_database.v_has_indexes,
                "v_has_checks": v_database.v_has_checks,
                "v_has_excludes": v_database.v_has_excludes,
                "v_has_rules": v_database.v_has_rules,
                "v_has_triggers": v_database.v_has_triggers,
                "v_has_partitions": v_database.v_has_partitions,
                "v_has_statistics": v_database.v_has_statistics,
                "v_oid": v_table["oid"],
            }
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_partitions_parents_postgresql/")
def get_partitions_parents(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_schema = json_object["p_schema"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryTablesPartitionsParents(False, v_schema)
        for v_table in v_tables.Rows:
            v_table_data = {
                "v_name": v_table["table_schema"] + "." + v_table["table_name"]
            }
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/get_partitions_children_postgresql/")
def get_partitions_children(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    v_list_tables = []

    try:
        v_tables = v_database.QueryTablesPartitionsChildren(v_table, v_schema)
        for v_table in v_tables.Rows:
            v_table_data = {
                "v_name": v_table["table_name"],
                "v_has_primary_keys": v_database.v_has_primary_keys,
                "v_has_foreign_keys": v_database.v_has_foreign_keys,
                "v_has_uniques": v_database.v_has_uniques,
                "v_has_indexes": v_database.v_has_indexes,
                "v_has_checks": v_database.v_has_checks,
                "v_has_excludes": v_database.v_has_excludes,
                "v_has_rules": v_database.v_has_rules,
                "v_has_triggers": v_database.v_has_triggers,
                "v_has_partitions": v_database.v_has_partitions,
                "v_has_statistics": v_database.v_has_statistics,
                "v_oid": v_table["oid"],
            }
            v_list_tables.append(v_table_data)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_list_tables

    return v_return


@app.post("/kill_backend_postgresql/")
def kill_backend(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_pid = json_object["p_pid"]

    try:
        v_database.Terminate(v_pid)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/template_select_postgresql/")
def template_select(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]
    v_kind = json_object["p_kind"]

    try:
        v_template = v_database.TemplateSelect(v_schema, v_table, v_kind).v_text
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = {"v_template": v_template}

    return v_return


@app.post("/template_insert_postgresql/")
def template_insert(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    try:
        v_template = v_database.TemplateInsert(v_schema, v_table).v_text
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = {"v_template": v_template}

    return v_return


@app.post("/template_update_postgresql/")
def template_update(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_table = json_object["p_table"]
    v_schema = json_object["p_schema"]

    try:
        v_template = v_database.TemplateUpdate(v_schema, v_table).v_text
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = {"v_template": v_template}

    return v_return


@app.post("/template_select_function_postgresql/")
def template_select_function(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_function = json_object["p_function"]
    v_functionid = json_object["p_functionid"]
    v_schema = json_object["p_schema"]

    try:
        v_template = v_database.TemplateSelectFunction(
            v_schema, v_function, v_functionid
        ).v_text
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = {"v_template": v_template}

    return v_return


@app.post("/template_call_procedure_postgresql/")
def template_call_procedure(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]
    v_procedure = json_object["p_procedure"]
    v_procedureid = json_object["p_procedureid"]
    v_schema = json_object["p_schema"]

    try:
        v_template = v_database.TemplateCallProcedure(
            v_schema, v_procedure, v_procedureid
        ).v_text
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = {"v_template": v_template}

    return v_return


@app.post("/get_version_postgresql/")
def get_version(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]
    v_tab_id = json_object["p_tab_id"]

    try:
        v_return["v_data"] = {"v_version": v_database.GetVersion()}
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/change_role_password_postgresql/")
def change_role_password(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_database_index = json_object["p_database_index"]

    try:
        v_database.ChangeRolePassword(json_object["p_role"], json_object["p_password"])
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    return v_return


@app.post("/get_object_description_postgresql/")
def get_object_description(
    user=Depends(dependencies.get_user),
    json_object=Depends(dependencies.parse_json_object),
    v_session=Depends(dependencies.get_omnidb_session),
    v_database=dependencies.require_database(),
    v_return=Depends(dependencies.get_default_return),
):

    v_oid = json_object["p_oid"]
    v_type = json_object["p_type"]
    v_position = json_object["p_position"]

    v_data = ""

    try:
        v_data = v_database.GetObjectDescription(v_type, v_oid, v_position)
    except Exception as exc:
        v_return["v_data"] = {"password_timeout": True, "message": str(exc)}
        v_return["v_error"] = True
        return v_return

    v_return["v_data"] = v_data

    return v_return
