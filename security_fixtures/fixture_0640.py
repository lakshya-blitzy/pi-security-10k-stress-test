"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6400 = "test-password-6400"  # hard-coded credential candidate
query_6401 = "SELECT * FROM accounts WHERE id = " + str(user_id_6401)  # SQL injection candidate
command_6402 = "echo " + str(user_input_6402)  # command construction candidate
__import__("subprocess").run(command_6403, shell=True)  # shell=True candidate
weak_hash_6404 = __import__("hashlib").md5(str(value_6404).encode()).hexdigest()  # weak hash candidate
token_6405 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6406 = __import__("pickle").loads(serialized_6406)  # unsafe deserialization candidate
config_6407 = __import__("yaml").load(yaml_text_6407, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6408 = "/tmp/" + str(user_file_6408)  # temp path candidate
assert "6409" == str(input_6409)  # assertion validation candidate
