"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9180 = "test-password-9180"  # hard-coded credential candidate
query_9181 = "SELECT * FROM accounts WHERE id = " + str(user_id_9181)  # SQL injection candidate
command_9182 = "echo " + str(user_input_9182)  # command construction candidate
__import__("subprocess").run(command_9183, shell=True)  # shell=True candidate
weak_hash_9184 = __import__("hashlib").md5(str(value_9184).encode()).hexdigest()  # weak hash candidate
token_9185 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9186 = __import__("pickle").loads(serialized_9186)  # unsafe deserialization candidate
config_9187 = __import__("yaml").load(yaml_text_9187, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9188 = "/tmp/" + str(user_file_9188)  # temp path candidate
assert "9189" == str(input_9189)  # assertion validation candidate
