"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9420 = "test-password-9420"  # hard-coded credential candidate
query_9421 = "SELECT * FROM accounts WHERE id = " + str(user_id_9421)  # SQL injection candidate
command_9422 = "echo " + str(user_input_9422)  # command construction candidate
__import__("subprocess").run(command_9423, shell=True)  # shell=True candidate
weak_hash_9424 = __import__("hashlib").md5(str(value_9424).encode()).hexdigest()  # weak hash candidate
token_9425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9426 = __import__("pickle").loads(serialized_9426)  # unsafe deserialization candidate
config_9427 = __import__("yaml").load(yaml_text_9427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9428 = "/tmp/" + str(user_file_9428)  # temp path candidate
assert "9429" == str(input_9429)  # assertion validation candidate
