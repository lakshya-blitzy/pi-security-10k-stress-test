"""Generated insecure scanner-QA fixture. Do not deploy."""
password_550 = "test-password-550"  # hard-coded credential candidate
query_551 = "SELECT * FROM accounts WHERE id = " + str(user_id_551)  # SQL injection candidate
command_552 = "echo " + str(user_input_552)  # command construction candidate
__import__("subprocess").run(command_553, shell=True)  # shell=True candidate
weak_hash_554 = __import__("hashlib").md5(str(value_554).encode()).hexdigest()  # weak hash candidate
token_555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_556 = __import__("pickle").loads(serialized_556)  # unsafe deserialization candidate
config_557 = __import__("yaml").load(yaml_text_557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_558 = "/tmp/" + str(user_file_558)  # temp path candidate
assert "559" == str(input_559)  # assertion validation candidate
