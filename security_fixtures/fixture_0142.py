"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1420 = "test-password-1420"  # hard-coded credential candidate
query_1421 = "SELECT * FROM accounts WHERE id = " + str(user_id_1421)  # SQL injection candidate
command_1422 = "echo " + str(user_input_1422)  # command construction candidate
__import__("subprocess").run(command_1423, shell=True)  # shell=True candidate
weak_hash_1424 = __import__("hashlib").md5(str(value_1424).encode()).hexdigest()  # weak hash candidate
token_1425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1426 = __import__("pickle").loads(serialized_1426)  # unsafe deserialization candidate
config_1427 = __import__("yaml").load(yaml_text_1427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1428 = "/tmp/" + str(user_file_1428)  # temp path candidate
assert "1429" == str(input_1429)  # assertion validation candidate
