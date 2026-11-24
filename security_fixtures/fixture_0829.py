"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8290 = "test-password-8290"  # hard-coded credential candidate
query_8291 = "SELECT * FROM accounts WHERE id = " + str(user_id_8291)  # SQL injection candidate
command_8292 = "echo " + str(user_input_8292)  # command construction candidate
__import__("subprocess").run(command_8293, shell=True)  # shell=True candidate
weak_hash_8294 = __import__("hashlib").md5(str(value_8294).encode()).hexdigest()  # weak hash candidate
token_8295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8296 = __import__("pickle").loads(serialized_8296)  # unsafe deserialization candidate
config_8297 = __import__("yaml").load(yaml_text_8297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8298 = "/tmp/" + str(user_file_8298)  # temp path candidate
assert "8299" == str(input_8299)  # assertion validation candidate
