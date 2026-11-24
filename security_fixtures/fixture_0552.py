"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5520 = "test-password-5520"  # hard-coded credential candidate
query_5521 = "SELECT * FROM accounts WHERE id = " + str(user_id_5521)  # SQL injection candidate
command_5522 = "echo " + str(user_input_5522)  # command construction candidate
__import__("subprocess").run(command_5523, shell=True)  # shell=True candidate
weak_hash_5524 = __import__("hashlib").md5(str(value_5524).encode()).hexdigest()  # weak hash candidate
token_5525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5526 = __import__("pickle").loads(serialized_5526)  # unsafe deserialization candidate
config_5527 = __import__("yaml").load(yaml_text_5527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5528 = "/tmp/" + str(user_file_5528)  # temp path candidate
assert "5529" == str(input_5529)  # assertion validation candidate
