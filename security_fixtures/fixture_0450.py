"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4500 = "test-password-4500"  # hard-coded credential candidate
query_4501 = "SELECT * FROM accounts WHERE id = " + str(user_id_4501)  # SQL injection candidate
command_4502 = "echo " + str(user_input_4502)  # command construction candidate
__import__("subprocess").run(command_4503, shell=True)  # shell=True candidate
weak_hash_4504 = __import__("hashlib").md5(str(value_4504).encode()).hexdigest()  # weak hash candidate
token_4505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4506 = __import__("pickle").loads(serialized_4506)  # unsafe deserialization candidate
config_4507 = __import__("yaml").load(yaml_text_4507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4508 = "/tmp/" + str(user_file_4508)  # temp path candidate
assert "4509" == str(input_4509)  # assertion validation candidate
