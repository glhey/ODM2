__author__ = 'Stephanie'


from ...base import serviceBase
from ..model import *
from sqlalchemy import func


class readCore(serviceBase):
    """queries to tables contained in the core schema"""

    """
    Variable
    """

    def getAllVariables(self):
        """Select all on Variables

        :return Variable Objects:
            :type list:
        """
        return self._session.query(Variable).all()

    def getVariableById(self, variableId):
        """Select by variableId

        :param variableId:
            :type Integer:
        :return Return matching Variable object filtered by variableId:
            :type Variable:
        """
        try:
            return self._session.query(Variable).filter_by(VariableID=variableId).one()
        except:
            return None

    def getVariableByCode(self, variableCode):
        """Select by variableCode

        :param variableCode:
            :type String:
        :return Return matching Variable Object filtered by variableCode:
            :type Variable:
        """
        try:
            return self._session.query(Variable).filter_by(VariableCode=variableCode).one()
        except:
            return None

    """
    Method
    """

    def getAllMethods(self):
        """Select all on Methods

        :return Method Objects:
            :type list:
        """
        return self._session.query(Method).all()

    def getMethodById(self, methodId):
        """Select by methodId

        :param methodId:
            :type Integer
        :return Return matching Method Object filtered by methodId:
            :type Method:
        """
        try:
            return self._session.query(Method).filter_by(MethodID=methodId).one()
        except:
            return None

    def getMethodByCode(self, methodCode):
        """Select by methodCode

        :param methodCode:
            :type String:
        :return Return matching Method Object filtered by method Code:
            :type Method:
        """
        try:
            return self._session.query(Method).filter_by(MethodCode=methodCode).one()
        except:
            return None

    """
    ProcessingLevel
    """

    def getAllProcessingLevel(self):
        """Select all on Processing Level

        :return ProcessingLevel Objects:
            :type list:
        """
        return self._session.query(Processinglevel).all()

    def getProcessingLevelById(self, processingId):
        """Select by processingId

        :param processingId:
            :type Integer:
        :return Return matching ProcessingLevel Object filtered by processingId:
            :type Processinglevel:
        """
        try:
            return self._session.query(Processinglevel).filter_by(ProcessingLevelID=processingId).one()
        except:
            return None


    def getProcessingLevelByCode(self, processingCode):
        """Select by processingCode

        :param processingCode:
            :type String(50):
        :return Return matching Processinglevel Object filtered by processingCode:
            :type Processinglevel:
        """
        try:
            return self._session.query(Processinglevel).filter_by(ProcessingLevelCode=str(processingCode)).first()
        except Exception, e:
            print e
            return None

    """
    Sampling Feature
    """

    def getAllSamplingFeature(self):
        """Select all on SamplingFeatures

        :return SamplingFeature Objects:
            :type list:
        """
        return self._session.query(Samplingfeature).from_statement("Select SamplingFeatureID\
                                                                        ,SamplingFeatureTypeCV\
                                                                        ,SamplingFeatureCode\
                                                                        ,SamplingFeatureName\
                                                                        ,SamplingFeatureDescription\
                                                                        ,SamplingFeatureGeotypeCV\
                                                                        ,Elevation_m\
                                                                        ,ElevationDatumCV\
                                                                        ,FeatureGeometry.STAsText() As FeatureGeometry\
                                                                     From ODM2Core.SamplingFeatures").all()
        #return self._session.query(m.Samplingfeature).all()

    def getSamplingFeatureById(self, samplingId):
        """Select by samplingId

        :param samplingId:
            :type Integer:
        :return Return matching SamplingFeature Object filtered by samplingId:
            :type SamplingFeature:
        """
        try:
            return self._session.query(Samplingfeature).from_statement("Select SamplingFeatureID\
                                                                        ,SamplingFeatureTypeCV\
                                                                        ,SamplingFeatureCode\
                                                                        ,SamplingFeatureName\
                                                                        ,SamplingFeatureDescription\
                                                                        ,SamplingFeatureGeotypeCV\
                                                                        ,Elevation_m\
                                                                        ,ElevationDatumCV\
                                                                        ,FeatureGeometry.STAsText() As FeatureGeometry\
                                                                     From ODM2Core.SamplingFeatures\
                                                                     Where SamplingFeatureID=\'%s\'"% samplingId).one()
        except:
            return None

    def getSamplingFeatureByCode(self, samplingCode):
        """Select by samplingCode

        :param samplingCode:
            :type String:
        :return Return matching SamplingFeature Object filtered by samplingId
            :type SamplingFeature:
        """
        try:
            return self._session.query(Samplingfeature).from_statement("Select SamplingFeatureID\
                                                                        ,SamplingFeatureTypeCV\
                                                                        ,SamplingFeatureCode\
                                                                        ,SamplingFeatureName\
                                                                        ,SamplingFeatureDescription\
                                                                        ,SamplingFeatureGeotypeCV\
                                                                        ,Elevation_m\
                                                                        ,ElevationDatumCV\
                                                                        ,FeatureGeometry.STAsText() As FeatureGeometry\
                                                                     From ODM2Core.SamplingFeatures\
                                                                     Where SamplingFeatureCode=\'%s\'"% samplingCode).one()
        except:
            return None

    """
    Unit
    """
    def getAllUnits(self):
        """Select all on Unit

        :return Unit Objects:
            :type list:
        """
        return self._session.query(Unit).all()


    def getUnitById(self, unitId):
        """Select by samplingId

        :param unitId:
            :type Integer:
        :return Return matching Unit Object filtered by UnitId:
            :type Unit:
        """
        try:
            return self._session.query(Unit).filter_by(UnitsID=unitId).one()
        except:
            return None

    def getUnitByName(self, unitName):


        try:
            return self._session.query(Unit).filter(Unit.UnitsName.ilike(unitName)).one()
        except:
            return None

    """
    Organization
    """
    def getAllOrganizations(self):
        """Select all on Organization

        :return Organization Objects:
            :type list:
        """
        return self._session.query(Organization).all()


    def getOrganizationById(self, orgId):
        """Select by orgId

        :param orgId:
            :type Integer:
        :return Return matching Unit Object filtered by orgId:
            :type Organization:
        """
        try:
            return self._session.query(Organization).filter_by(OrganizationID=orgId).one()
        except:
            return None


    def getOrganizationByCode(self, orgCode):
        """Select by orgCode

        :param orgCode:
            :type String:
        :return Return matching Organization Object filtered by orgCode
            :type Organization:
        """
        try:
            return self._session.query(Organization).filter_by(OrganizationCode=orgCode).one()
        except:
            return None
    """
    Person
    """
    def getAllPerson(self):
        """Select all on Person

        :return Person Objects:
            :type list:
        """
        return self._session.query(Person).all()


    def getPersonById(self, personId):
        """Select by personId

        :param personId:
            :type Integer:
        :return Return matching Person Object filtered by personId:
            :type Person:
        """
        try:
            return self._session.query(Person).filter_by(PersonID=personId).one()
        except:
            return None

    def getPersonByName(self, personfirst, personlast):
        """Select by person name, last name combination

        :param personfirst: first name of person
        :param personlast: last name of person
        :return Return matching Person Object:
            :type Person:
        """
        try:
            return self._session.query(Person).filter(Person.PersonFirstName.ilike(personfirst)). \
                                                 filter(Person.PersonLastName.ilike(personlast)).one()
        except:
            return None

    def getAffiliationByPersonAndOrg(self,personfirst,personlast,orgcode):
        """
        Select all affiliation of person
        :param personfirst: first name of person
        :param personlast: last name of person
        :param orgcode: organization code (e.g. uwrl)
        :return: ODM2Core.Affiliation
        """

        try:
            return self._session.query(Affiliation).filter(Organization.OrganizationCode.ilike(orgcode)) \
                                                    .filter(Person.PersonFirstName.ilike(personfirst)) \
                                                   .filter(Person.PersonLastName.ilike(personlast)).one()
        except:
            return None

    def getAffiliationsByPerson(self,personfirst,personlast):
        """
        Select all affiliation of person
        :param personfirst: first name of person
        :param personlast: last name of person
        :return: [ODM2Core.Affiliation]
        """

        try:
            return self._session.query(Affiliation).filter(Person.PersonFirstName.ilike(personfirst)) \
                                                   .filter(Person.PersonLastName.ilike(personlast)).all()
        except:
            return None

    def getDataSetByCode(self,dscode):

        try:
            return self._session.query(Dataset).filer(Dataset.DataSetCode.ilike(dscode)).one()
        except:
            return None

    def getSamplingFeatureByGeometry(self,wkt_geometry):

        try:
            #ST_Equals(geometry, geometry)
            return self._session.query(Samplingfeature).filter(func.ST_AsText(Samplingfeature.FeatureGeometry) == func.ST_AsText(wkt_geometry)).one()
        except Exception, e:
            print e
            return None