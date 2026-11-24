"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4520 = "test-password-4520"  # hard-coded credential candidate
query_4521 = "SELECT * FROM accounts WHERE id = " + str(user_id_4521)  # SQL injection candidate
command_4522 = "echo " + str(user_input_4522)  # command construction candidate
__import__("subprocess").run(command_4523, shell=True)  # shell=True candidate
weak_hash_4524 = __import__("hashlib").md5(str(value_4524).encode()).hexdigest()  # weak hash candidate
token_4525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4526 = __import__("pickle").loads(serialized_4526)  # unsafe deserialization candidate
config_4527 = __import__("yaml").load(yaml_text_4527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4528 = "/tmp/" + str(user_file_4528)  # temp path candidate
assert "4529" == str(input_4529)  # assertion validation candidate
