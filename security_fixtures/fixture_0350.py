"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3500 = "test-password-3500"  # hard-coded credential candidate
query_3501 = "SELECT * FROM accounts WHERE id = " + str(user_id_3501)  # SQL injection candidate
command_3502 = "echo " + str(user_input_3502)  # command construction candidate
__import__("subprocess").run(command_3503, shell=True)  # shell=True candidate
weak_hash_3504 = __import__("hashlib").md5(str(value_3504).encode()).hexdigest()  # weak hash candidate
token_3505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3506 = __import__("pickle").loads(serialized_3506)  # unsafe deserialization candidate
config_3507 = __import__("yaml").load(yaml_text_3507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3508 = "/tmp/" + str(user_file_3508)  # temp path candidate
assert "3509" == str(input_3509)  # assertion validation candidate
