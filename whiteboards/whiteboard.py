class AssayClient:
    def __init__(self):
        self.server = defaultAssayServer

    def makeRequest(self, requestType, bodyDict, getQuery='',
                    expectStringResponse=False):
        requestUrl = self.server + '/' + requestType
        request = None

        # DEBUG
        sys.stderr.write('requestUrl: %s\n' % requestUrl)

        if (getQuery != ''):
            requestUrl += ('?' + getQuery)

        # DEBUG
        sys.stderr.write('requestUrl with query: %s\n' % requestUrl)

        if (bodyDict is None):
            request = urllib2.Request(url = requestUrl)
        else:
            bodyJson = json.dumps(bodyDict)
            request = urllib2.Request(url = requestUrl, data = bodyJson)

        # DEBUG
        sys.stderr.write('About to add Content-Type\n')

        request.add_header('Content-Type', 'application/json')

        # DEBUG
        sys.stderr.write('About to make request\n')

        hndl = urllib2.urlopen(request)

        # DEBUG
        sys.stderr.write('About to get response\n')

        try:
            response = hndl.read()
            hndl.close()
        except Exception as e:
            print(e)
            sys.stderr.write('Server unhappy with: %s request\n' % requestType)
            raise e

        if (expectStringResponse):
            # DEBUG
            sys.stderr.write('About to return string response\n')

            return response

        # DEBUG
        sys.stderr.write('About to parse response as JSON\n')

        responseJson = json.loads(response)

        # DEBUG
        print responseJson
        sys.stderr.write('About to extract result from JSON\n')

        resultJson = responseJson['result']
        return resultJson


    def updateProgress(self, analysisId, progressState):
        resultStr = ''
        bodyDict = dict()
        bodyDict[analysisIdKey] = analysisId
        bodyDict[analysisProgressKey] = progressState

        try:
            resultStr = self.makeRequest(updateProgressRequestType,
                                         bodyDict, expectStringResponse=True)
        except Exception as e:
            print(e)
            print 'Error setting state of analysis %s to %s' % (analysisId,
                                                                progressState)
            return False

        print 'State of analysis %s set to %s' % (analysisId, progressState)
        print 'Result from server: %s' % resultStr
        return True