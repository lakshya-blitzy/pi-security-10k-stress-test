"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9200 = "test-password-9200"  # hard-coded credential candidate
query_9201 = "SELECT * FROM accounts WHERE id = " + str(user_id_9201)  # SQL injection candidate
command_9202 = "echo " + str(user_input_9202)  # command construction candidate
__import__("subprocess").run(command_9203, shell=True)  # shell=True candidate
weak_hash_9204 = __import__("hashlib").md5(str(value_9204).encode()).hexdigest()  # weak hash candidate
token_9205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9206 = __import__("pickle").loads(serialized_9206)  # unsafe deserialization candidate
config_9207 = __import__("yaml").load(yaml_text_9207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9208 = "/tmp/" + str(user_file_9208)  # temp path candidate
assert "9209" == str(input_9209)  # assertion validation candidate
