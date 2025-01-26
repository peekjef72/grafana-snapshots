from verlib2 import Version

from grafana_snapshots.dataresults.dataresults import dataresults

datasource_type = 'prometheus'
api_version = Version('11.4.0')


#***************************************************************************************
def test_data_ts_range_panel_stat(build_config):
    # read the datasource
    content = build_config.readResponse('queries/grafana_10/prometheus/metric_range_expr.json')
    format = 'time_series'
    # read the panel
    panel = build_config.readPanel('panels/grafana_10/stat_range_met_expr.json')

    dataRes = dataresults( 
        type=datasource_type,
        format=format,
        results=content,
        version=api_version,
        panel=panel)
    snapshotData = dataRes.get_snapshotData(build_config.targets)

    assert snapshotData is not None, "invalid data"
    # one ts results
    assert len(snapshotData) == 1 , 'invalid snapshot data length wanted 1 but is {}'.format(len(snapshotData))
    # two fields in result: ts and value
    assert len(snapshotData[0]['fields']) == 2 , 'invalid snapshot data fields length wanted 2 but is {}'.format(len(snapshotData))
    assert snapshotData[0]['refId'] == 'B', 'invalid snapshot data refId wanted B but is {}'.format(snapshotData[0]['refId'])