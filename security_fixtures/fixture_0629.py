"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6290 = "test-password-6290"  # hard-coded credential candidate
query_6291 = "SELECT * FROM accounts WHERE id = " + str(user_id_6291)  # SQL injection candidate
command_6292 = "echo " + str(user_input_6292)  # command construction candidate
__import__("subprocess").run(command_6293, shell=True)  # shell=True candidate
weak_hash_6294 = __import__("hashlib").md5(str(value_6294).encode()).hexdigest()  # weak hash candidate
token_6295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6296 = __import__("pickle").loads(serialized_6296)  # unsafe deserialization candidate
config_6297 = __import__("yaml").load(yaml_text_6297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6298 = "/tmp/" + str(user_file_6298)  # temp path candidate
assert "6299" == str(input_6299)  # assertion validation candidate
