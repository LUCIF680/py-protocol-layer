import json
import uuid

from flask import request
from flask_restx import Namespace, Resource

from main import constant
from main.config import get_config_by_name
from main.models.catalog import SearchType
from main.repository.ack_response import get_ack_response
from main.service import send_message_to_queue_for_given_request
from main.service.common import add_bpp_response, dump_request_payload, update_dumped_request_with_response
from main.service.search import add_search_catalogues, dump_on_search_payload, add_incremental_search_catalogues
from main.service.utils import validate_auth_header
from main.utils.validation import validate_payload_schema_based_on_version

ondc_network_namespace = Namespace('ondc_network', description='ONDC Network Namespace')


@ondc_network_namespace.route("/v1/on_search")
class GatewayOnSearch(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        # validate schema based on context version
        resp = validate_payload_schema_based_on_version(request_payload, 'on_search')
        if resp is None:
            request_type = request.headers.get("X-ONDC-Search-Response", "full")
            if get_config_by_name('QUEUE_ENABLE'):
                unique_id = str(uuid.uuid4())
                request_payload["id"] = unique_id
                dump_on_search_payload(request_payload)
                message = {
                    "unique_id": unique_id,
                    "request_type": request_type,
                }
                send_message_to_queue_for_given_request(message)
                return get_ack_response(request_payload[constant.CONTEXT], ack=True)
            else:
                if request_type == SearchType.FULL.value:
                    return add_search_catalogues(request_payload)
                elif request_type == SearchType.INC.value:
                    return add_incremental_search_catalogues(request_payload)
            # add search catalogs based on context version
            # return add_search_catalogues(request_payload)
        else:
            return resp


@ondc_network_namespace.route("/v1/on_select")
class AddSelectResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_select')
        if resp is None:
            entry_object_id = dump_request_payload("on_select", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_select")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_init")
class AddInitResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_init')
        if resp is None:
            entry_object_id = dump_request_payload("on_init", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_init")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_confirm")
class AddConfirmResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_confirm')
        if resp is None:
            entry_object_id = dump_request_payload("on_confirm", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_confirm")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_cancel")
class AddCancelResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_cancel')
        if resp is None:
            entry_object_id = dump_request_payload("on_cancel", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_cancel")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/cancellation_reasons")
class AddCancellationReasonsResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_cancellation_reasons')
        if resp is None:
            entry_object_id = dump_request_payload("on_cancellation_reasons", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_cancellation_reasons")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_issue")
class AddIssueResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_issue')
        if resp is None:
            entry_object_id = dump_request_payload("on_issue", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_issue")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_issue_status")
class AddIssueStatusResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_issue_status')
        if resp is None:
            entry_object_id = dump_request_payload("on_issue_status", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_issue_status")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_rating")
class AddRatingResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_rating')
        if resp is None:
            entry_object_id = dump_request_payload("on_rating", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_rating")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_status")
class AddStatusResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_status')
        if resp is None:
            entry_object_id = dump_request_payload("on_status", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_status")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_support")
class AddSupportResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_support')
        if resp is None:
            entry_object_id = dump_request_payload("on_support", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_support")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_track")
class AddTrackResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_track')
        if resp is None:
            entry_object_id = dump_request_payload("on_track", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_track")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp


@ondc_network_namespace.route("/v1/on_update")
class AddUpdateResponse(Resource):

    @validate_auth_header
    def post(self):
        request_payload = request.get_json()
        resp = validate_payload_schema_based_on_version(request_payload, 'on_update')
        if resp is None:
            entry_object_id = dump_request_payload("on_update", request_payload)
            resp = add_bpp_response(request_payload, request_type="on_update")
            update_dumped_request_with_response(entry_object_id, resp)
            return resp
        else:
            return resp
