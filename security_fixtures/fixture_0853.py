"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8530 = "test-password-8530"  # hard-coded credential candidate
query_8531 = "SELECT * FROM accounts WHERE id = " + str(user_id_8531)  # SQL injection candidate
command_8532 = "echo " + str(user_input_8532)  # command construction candidate
__import__("subprocess").run(command_8533, shell=True)  # shell=True candidate
weak_hash_8534 = __import__("hashlib").md5(str(value_8534).encode()).hexdigest()  # weak hash candidate
token_8535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8536 = __import__("pickle").loads(serialized_8536)  # unsafe deserialization candidate
config_8537 = __import__("yaml").load(yaml_text_8537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8538 = "/tmp/" + str(user_file_8538)  # temp path candidate
assert "8539" == str(input_8539)  # assertion validation candidate
