"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4530 = "test-password-4530"  # hard-coded credential candidate
query_4531 = "SELECT * FROM accounts WHERE id = " + str(user_id_4531)  # SQL injection candidate
command_4532 = "echo " + str(user_input_4532)  # command construction candidate
__import__("subprocess").run(command_4533, shell=True)  # shell=True candidate
weak_hash_4534 = __import__("hashlib").md5(str(value_4534).encode()).hexdigest()  # weak hash candidate
token_4535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4536 = __import__("pickle").loads(serialized_4536)  # unsafe deserialization candidate
config_4537 = __import__("yaml").load(yaml_text_4537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4538 = "/tmp/" + str(user_file_4538)  # temp path candidate
assert "4539" == str(input_4539)  # assertion validation candidate
