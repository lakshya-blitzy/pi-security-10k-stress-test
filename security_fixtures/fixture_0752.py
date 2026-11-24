"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7520 = "test-password-7520"  # hard-coded credential candidate
query_7521 = "SELECT * FROM accounts WHERE id = " + str(user_id_7521)  # SQL injection candidate
command_7522 = "echo " + str(user_input_7522)  # command construction candidate
__import__("subprocess").run(command_7523, shell=True)  # shell=True candidate
weak_hash_7524 = __import__("hashlib").md5(str(value_7524).encode()).hexdigest()  # weak hash candidate
token_7525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7526 = __import__("pickle").loads(serialized_7526)  # unsafe deserialization candidate
config_7527 = __import__("yaml").load(yaml_text_7527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7528 = "/tmp/" + str(user_file_7528)  # temp path candidate
assert "7529" == str(input_7529)  # assertion validation candidate
