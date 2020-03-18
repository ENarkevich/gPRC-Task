// Code generated by protoc-gen-grpc-gateway. DO NOT EDIT.
// source: data.proto

/*
Package data is a reverse proxy.

It translates gRPC into RESTful JSON APIs.
*/
package data

import (
	"context"
	"io"
	"net/http"

	"github.com/golang/protobuf/descriptor"
	"github.com/golang/protobuf/proto"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"github.com/grpc-ecosystem/grpc-gateway/utilities"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/grpclog"
	"google.golang.org/grpc/status"
)

// Suppress "imported and not used" errors
var _ codes.Code
var _ io.Reader
var _ status.Status
var _ = runtime.String
var _ = utilities.NewDoubleArray
var _ = descriptor.ForMessage

func request_CroppImage_Cropp_0(ctx context.Context, marshaler runtime.Marshaler, client CroppImageClient, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq InputImage
	var metadata runtime.ServerMetadata

	newReader, berr := utilities.IOReaderFactory(req.Body)
	if berr != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", berr)
	}
	if err := marshaler.NewDecoder(newReader()).Decode(&protoReq); err != nil && err != io.EOF {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := client.Cropp(ctx, &protoReq, grpc.Header(&metadata.HeaderMD), grpc.Trailer(&metadata.TrailerMD))
	return msg, metadata, err

}

func local_request_CroppImage_Cropp_0(ctx context.Context, marshaler runtime.Marshaler, server CroppImageServer, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq InputImage
	var metadata runtime.ServerMetadata

	newReader, berr := utilities.IOReaderFactory(req.Body)
	if berr != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", berr)
	}
	if err := marshaler.NewDecoder(newReader()).Decode(&protoReq); err != nil && err != io.EOF {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := server.Cropp(ctx, &protoReq)
	return msg, metadata, err

}

func request_ConcatenateImage_Concatenate_0(ctx context.Context, marshaler runtime.Marshaler, client ConcatenateImageClient, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq ImageParts
	var metadata runtime.ServerMetadata

	newReader, berr := utilities.IOReaderFactory(req.Body)
	if berr != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", berr)
	}
	if err := marshaler.NewDecoder(newReader()).Decode(&protoReq); err != nil && err != io.EOF {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := client.Concatenate(ctx, &protoReq, grpc.Header(&metadata.HeaderMD), grpc.Trailer(&metadata.TrailerMD))
	return msg, metadata, err

}

func local_request_ConcatenateImage_Concatenate_0(ctx context.Context, marshaler runtime.Marshaler, server ConcatenateImageServer, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq ImageParts
	var metadata runtime.ServerMetadata

	newReader, berr := utilities.IOReaderFactory(req.Body)
	if berr != nil {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", berr)
	}
	if err := marshaler.NewDecoder(newReader()).Decode(&protoReq); err != nil && err != io.EOF {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := server.Concatenate(ctx, &protoReq)
	return msg, metadata, err

}

// RegisterCroppImageHandlerServer registers the http handlers for service CroppImage to "mux".
// UnaryRPC     :call CroppImageServer directly.
// StreamingRPC :currently unsupported pending https://github.com/grpc/grpc-go/issues/906.
func RegisterCroppImageHandlerServer(ctx context.Context, mux *runtime.ServeMux, server CroppImageServer) error {

	mux.Handle("POST", pattern_CroppImage_Cropp_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		rctx, err := runtime.AnnotateIncomingContext(ctx, mux, req)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := local_request_CroppImage_Cropp_0(rctx, inboundMarshaler, server, req, pathParams)
		ctx = runtime.NewServerMetadataContext(ctx, md)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_CroppImage_Cropp_0(ctx, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

// RegisterConcatenateImageHandlerServer registers the http handlers for service ConcatenateImage to "mux".
// UnaryRPC     :call ConcatenateImageServer directly.
// StreamingRPC :currently unsupported pending https://github.com/grpc/grpc-go/issues/906.
func RegisterConcatenateImageHandlerServer(ctx context.Context, mux *runtime.ServeMux, server ConcatenateImageServer) error {

	mux.Handle("POST", pattern_ConcatenateImage_Concatenate_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		rctx, err := runtime.AnnotateIncomingContext(ctx, mux, req)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := local_request_ConcatenateImage_Concatenate_0(rctx, inboundMarshaler, server, req, pathParams)
		ctx = runtime.NewServerMetadataContext(ctx, md)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_ConcatenateImage_Concatenate_0(ctx, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

// RegisterCroppImageHandlerFromEndpoint is same as RegisterCroppImageHandler but
// automatically dials to "endpoint" and closes the connection when "ctx" gets done.
func RegisterCroppImageHandlerFromEndpoint(ctx context.Context, mux *runtime.ServeMux, endpoint string, opts []grpc.DialOption) (err error) {
	conn, err := grpc.Dial(endpoint, opts...)
	if err != nil {
		return err
	}
	defer func() {
		if err != nil {
			if cerr := conn.Close(); cerr != nil {
				grpclog.Infof("Failed to close conn to %s: %v", endpoint, cerr)
			}
			return
		}
		go func() {
			<-ctx.Done()
			if cerr := conn.Close(); cerr != nil {
				grpclog.Infof("Failed to close conn to %s: %v", endpoint, cerr)
			}
		}()
	}()

	return RegisterCroppImageHandler(ctx, mux, conn)
}

// RegisterCroppImageHandler registers the http handlers for service CroppImage to "mux".
// The handlers forward requests to the grpc endpoint over "conn".
func RegisterCroppImageHandler(ctx context.Context, mux *runtime.ServeMux, conn *grpc.ClientConn) error {
	return RegisterCroppImageHandlerClient(ctx, mux, NewCroppImageClient(conn))
}

// RegisterCroppImageHandlerClient registers the http handlers for service CroppImage
// to "mux". The handlers forward requests to the grpc endpoint over the given implementation of "CroppImageClient".
// Note: the gRPC framework executes interceptors within the gRPC handler. If the passed in "CroppImageClient"
// doesn't go through the normal gRPC flow (creating a gRPC client etc.) then it will be up to the passed in
// "CroppImageClient" to call the correct interceptors.
func RegisterCroppImageHandlerClient(ctx context.Context, mux *runtime.ServeMux, client CroppImageClient) error {

	mux.Handle("POST", pattern_CroppImage_Cropp_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		rctx, err := runtime.AnnotateContext(ctx, mux, req)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := request_CroppImage_Cropp_0(rctx, inboundMarshaler, client, req, pathParams)
		ctx = runtime.NewServerMetadataContext(ctx, md)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_CroppImage_Cropp_0(ctx, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

var (
	pattern_CroppImage_Cropp_0 = runtime.MustPattern(runtime.NewPattern(1, []int{2, 0}, []string{"cropp"}, "", runtime.AssumeColonVerbOpt(true)))
)

var (
	forward_CroppImage_Cropp_0 = runtime.ForwardResponseMessage
)

// RegisterConcatenateImageHandlerFromEndpoint is same as RegisterConcatenateImageHandler but
// automatically dials to "endpoint" and closes the connection when "ctx" gets done.
func RegisterConcatenateImageHandlerFromEndpoint(ctx context.Context, mux *runtime.ServeMux, endpoint string, opts []grpc.DialOption) (err error) {
	conn, err := grpc.Dial(endpoint, opts...)
	if err != nil {
		return err
	}
	defer func() {
		if err != nil {
			if cerr := conn.Close(); cerr != nil {
				grpclog.Infof("Failed to close conn to %s: %v", endpoint, cerr)
			}
			return
		}
		go func() {
			<-ctx.Done()
			if cerr := conn.Close(); cerr != nil {
				grpclog.Infof("Failed to close conn to %s: %v", endpoint, cerr)
			}
		}()
	}()

	return RegisterConcatenateImageHandler(ctx, mux, conn)
}

// RegisterConcatenateImageHandler registers the http handlers for service ConcatenateImage to "mux".
// The handlers forward requests to the grpc endpoint over "conn".
func RegisterConcatenateImageHandler(ctx context.Context, mux *runtime.ServeMux, conn *grpc.ClientConn) error {
	return RegisterConcatenateImageHandlerClient(ctx, mux, NewConcatenateImageClient(conn))
}

// RegisterConcatenateImageHandlerClient registers the http handlers for service ConcatenateImage
// to "mux". The handlers forward requests to the grpc endpoint over the given implementation of "ConcatenateImageClient".
// Note: the gRPC framework executes interceptors within the gRPC handler. If the passed in "ConcatenateImageClient"
// doesn't go through the normal gRPC flow (creating a gRPC client etc.) then it will be up to the passed in
// "ConcatenateImageClient" to call the correct interceptors.
func RegisterConcatenateImageHandlerClient(ctx context.Context, mux *runtime.ServeMux, client ConcatenateImageClient) error {

	mux.Handle("POST", pattern_ConcatenateImage_Concatenate_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		rctx, err := runtime.AnnotateContext(ctx, mux, req)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := request_ConcatenateImage_Concatenate_0(rctx, inboundMarshaler, client, req, pathParams)
		ctx = runtime.NewServerMetadataContext(ctx, md)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_ConcatenateImage_Concatenate_0(ctx, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

var (
	pattern_ConcatenateImage_Concatenate_0 = runtime.MustPattern(runtime.NewPattern(1, []int{2, 0}, []string{"concatenate"}, "", runtime.AssumeColonVerbOpt(true)))
)

var (
	forward_ConcatenateImage_Concatenate_0 = runtime.ForwardResponseMessage
)