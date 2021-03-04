from tests.common.ixia.ixia_fixtures import snappi_api
from tests.common.ixia.ixia_fixtures import (
    ixia_api_serv_ip, ixia_api_serv_port, tgen_ports)
from files.helper import run_bgp_convergence_test
from tests.common.fixtures.conn_graph_facts import (
    conn_graph_facts, fanout_graph_facts)
import pytest

@pytest.mark.parametrize('multipath',[2])
@pytest.mark.parametrize('convergence_test_iterations',[1])
def test_bgp_convergence(snappi_api,
                        duthost,
                        tgen_ports,
                        conn_graph_facts,
                        fanout_graph_facts,
                        multipath,
                        convergence_test_iterations):


    #convergence_test_iterations and multipath values can be modified as per user preference
    run_bgp_convergence_test(snappi_api,
                            duthost,
                            tgen_ports,
                            convergence_test_iterations,
                            multipath)
    
#this is just to check