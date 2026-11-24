"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6230 = "test-password-6230"  # hard-coded credential candidate
query_6231 = "SELECT * FROM accounts WHERE id = " + str(user_id_6231)  # SQL injection candidate
command_6232 = "echo " + str(user_input_6232)  # command construction candidate
__import__("subprocess").run(command_6233, shell=True)  # shell=True candidate
weak_hash_6234 = __import__("hashlib").md5(str(value_6234).encode()).hexdigest()  # weak hash candidate
token_6235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6236 = __import__("pickle").loads(serialized_6236)  # unsafe deserialization candidate
config_6237 = __import__("yaml").load(yaml_text_6237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6238 = "/tmp/" + str(user_file_6238)  # temp path candidate
assert "6239" == str(input_6239)  # assertion validation candidate
