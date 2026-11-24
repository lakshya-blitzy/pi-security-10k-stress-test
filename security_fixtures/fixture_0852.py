"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8520 = "test-password-8520"  # hard-coded credential candidate
query_8521 = "SELECT * FROM accounts WHERE id = " + str(user_id_8521)  # SQL injection candidate
command_8522 = "echo " + str(user_input_8522)  # command construction candidate
__import__("subprocess").run(command_8523, shell=True)  # shell=True candidate
weak_hash_8524 = __import__("hashlib").md5(str(value_8524).encode()).hexdigest()  # weak hash candidate
token_8525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8526 = __import__("pickle").loads(serialized_8526)  # unsafe deserialization candidate
config_8527 = __import__("yaml").load(yaml_text_8527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8528 = "/tmp/" + str(user_file_8528)  # temp path candidate
assert "8529" == str(input_8529)  # assertion validation candidate
