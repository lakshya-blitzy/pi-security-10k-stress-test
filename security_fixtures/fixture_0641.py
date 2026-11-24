"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6410 = "test-password-6410"  # hard-coded credential candidate
query_6411 = "SELECT * FROM accounts WHERE id = " + str(user_id_6411)  # SQL injection candidate
command_6412 = "echo " + str(user_input_6412)  # command construction candidate
__import__("subprocess").run(command_6413, shell=True)  # shell=True candidate
weak_hash_6414 = __import__("hashlib").md5(str(value_6414).encode()).hexdigest()  # weak hash candidate
token_6415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6416 = __import__("pickle").loads(serialized_6416)  # unsafe deserialization candidate
config_6417 = __import__("yaml").load(yaml_text_6417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6418 = "/tmp/" + str(user_file_6418)  # temp path candidate
assert "6419" == str(input_6419)  # assertion validation candidate
