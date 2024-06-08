FROM grafana/grafana-oss:10.3.1

##################################################################
## CONFIGURATION
##################################################################

## Set Grafana options
ENV GF_ENABLE_GZIP=true
ENV GF_USERS_DEFAULT_THEME=dark
ENV GF_USERS_DEFAULT_LANGUAGE=fr-FR

## Enable Anonymous Authentication
ENV GF_AUTH_ANONYMOUS_ENABLED=true
#Activate the ROLE VIEWER as Default
ENV GF_AUTH_ANONYMOUS_ORG_ROLE=Viewer
#Disable the AUTH Method
ENV GF_AUTH_BASIC_ENABLED=false
 #Disable the login on show
ENV GF_AUTH_DISABLE_LOGIN_FORM=true
#Diabled the menuENV GF_AUTH_BASIC_ENABLED=false #Disable the AUTH Method
ENV GF_AUTH_DISABLE_SIGNOUT_MENU=true
#Disable the login on show
ENV GF_AUTH_DISABLE_LOGIN_FORM=true
#Diabled the menu
ENV GF_AUTH_DISABLE_SIGNOUT_MENU=true

## Disable Sanitize
ENV GF_PANELS_DISABLE_SANITIZE_HTML=true

## Disable Explore
ENV GF_EXPLORE_ENABLED=false

# Updates Check
ENV GF_ANALYTICS_CHECK_FOR_UPDATES=false

## Disable snapshots
ENV GF_SNAPSHOTS_ENABLED=false

## Set Home Dashboard
ENV GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH=/var/lib/grafana/dashboards/R3C_General.json

## Paths
ENV GF_PATHS_PROVISIONING="/etc/grafana/provisioning"
#ENV GF_PATHS_PLUGINS="/var/lib/grafana/plugins"

#Add the configuration
ADD ./provisioning /etc/grafana/provisioning
#Add the Dashboard
ADD ./dashboards /var/lib/grafana/dashboards

ENV GF_INSTALL_PLUGINS=volkovlabs-form-panel

##################################################################
## COPY ARTIFACTS
##################################################################

COPY entrypoint.sh /

## Copy Provisioning
#COPY --chown=grafana:root provisioning $GF_PATHS_PROVISIONING

##################################################################
## Customization depends on the Grafana version
## May work or not work for the version different from the current
## Check GitHub file history for the previous Grafana versions
##################################################################
USER root

##################################################################
## VISUAL
##################################################################

## Replace Favicon and Apple Touch
COPY img/R3C_Logo_fav32.png /usr/share/grafana/public/img/fav32.png
COPY img/R3C_Logo_fav32.png /usr/share/grafana/public/img/apple-touch-icon.png

## Replace Logo
COPY img/R3C_Logo_Sans_baseline.svg /usr/share/grafana/public/img/grafana_icon.svg
COPY img/R3C_Logo_Sans_baseline.svg /usr/share/grafana/public/img/grafana_com_auth_icon.svg
COPY img/R3C_Logo_Sans_baseline.svg /usr/share/grafana/public/img/icons/mono/grafana.svg
## Update Background
#COPY img/background.svg /usr/share/grafana/public/img/g8_login_dark.svg
#COPY img/background.svg /usr/share/grafana/public/img/g8_login_light.svg

##################################################################
## HANDS-ON
##################################################################

# Update Title
RUN sed -i 's|<title>\[\[.AppTitle\]\]</title>|<title>R3C</title>|g' /usr/share/grafana/public/views/index.html

## Update Help menu
RUN sed -i "s|\[\[.NavTree\]\],|nav,|g; \
    s|window.grafanaBootData = {| \
    let nav = [[.NavTree]]; \
    const alerting = nav.find((element) => element.id === 'alerting'); \
    if (alerting) { alerting['url'] = '/alerting/list'; } \
    const dashboards = nav.find((element) => element.id === 'dashboards/browse'); \
    if (dashboards) { dashboards['children'] = [];} \
    const connections = nav.find((element) => element.id === 'connections'); \
    if (connections) { connections['url'] = '/datasources'; connections['children'].shift(); } \
    const help = nav.find((element) => element.id === 'help'); \
    if (help) { help['subTitle'] = 'Grafana OSS'; help['children'] = [];} \
    window.grafanaBootData = {|g" \
    /usr/share/grafana/public/views/index.html

## Update Title
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|AppTitle="Grafana"|AppTitle="R3C"|g' {} \;

## Update Login Title
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|LoginTitle="Welcome to Grafana"|LoginTitle="Réseau de capteurs pour la chiroptérologie"|g' {} \;

## Remove Documentation, Support, Community in the Footer
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|\[{target:"_blank",id:"documentation".*grafana_footer"}\]|\[\]|g' {} \;

## Remove Edition in the Footer
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|({target:"_blank",id:"license",.*licenseUrl})|()|g' {} \;

## Remove Version in the Footer
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|({target:"_blank",id:"version",.*CHANGELOG.md":void 0})|()|g' {} \;

## Remove News icon
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|..createElement(....,{className:.,onClick:.,iconOnly:!0,icon:"rss","aria-label":"News"})|null|g' {} \;

## Remove Open Source icon
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|.push({target:"_blank",id:"version",text:`${..edition}${.}`,url:..licenseUrl,icon:"external-link-alt"})||g' {} \;

##################################################################
## CLEANING Remove Native Data Sources
##################################################################

## Time series databases / Elasticsearch
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/elasticsearch
RUN rm -rf /usr/share/grafana/public/build/elasticsearch*

## Time series databases / Graphite
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/graphite
RUN rm -rf /usr/share/grafana/public/build/graphite*

## Time series databases / OpenTSDB
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/opentsdb
RUN rm -rf /usr/share/grafana/public/build/opentsdb*

## Time series databases / InfluxDB
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/influxdb
RUN rm -rf /usr/share/grafana/public/build/influxdb*

## SQL / Microsoft SQL Server
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/mssql
RUN rm -rf /usr/share/grafana/public/build/mssql*

## SQL / MySQL
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/mysql
RUN rm -rf /usr/share/grafana/public/build/mysql*

## Distributed tracing / Tempo
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/tempo
RUN rm -rf /usr/share/grafana/public/build/tempo*

## Distributed tracing / Jaeger
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/jaeger
RUN rm -rf /usr/share/grafana/public/build/jaeger*

## Distributed tracing / Zipkin
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/zipkin
RUN rm -rf /usr/share/grafana/public/build/zipkin*

## Cloud / Azure Monitor
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/azuremonitor
RUN rm -rf /usr/share/grafana/public/build/azureMonitor*

## Cloud / CloudWatch
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/cloudwatch
RUN rm -rf /usr/share/grafana/public/build/cloudwatch*

## Cloud / Google Cloud Monitoring
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/cloud-monitoring
RUN rm -rf /usr/share/grafana/public/build/cloudMonitoring*

## Profiling / Parca
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/parca
RUN rm -rf /usr/share/grafana/public/build/parca*

## Profiling / Phlare
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/phlare
RUN rm -rf /usr/share/grafana/public/build/phlare*

## Profiling / Pyroscope
RUN rm -rf /usr/share/grafana/public/app/plugins/datasource/grafana-pyroscope-datasource
RUN rm -rf /usr/share/grafana/public/build/pyroscope*

## Remove Cloud and Enterprise categories
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|.id==="enterprise"|.id==="notanenterprise"|g' {} \;
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|.id==="cloud"|.id==="notacloud"|g' {} \;

USER grafana

## Entrypoint
ENTRYPOINT [ "/bin/bash", "/entrypoint.sh" ]
