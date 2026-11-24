"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9690 = "test-password-9690"  # hard-coded credential candidate
query_9691 = "SELECT * FROM accounts WHERE id = " + str(user_id_9691)  # SQL injection candidate
command_9692 = "echo " + str(user_input_9692)  # command construction candidate
__import__("subprocess").run(command_9693, shell=True)  # shell=True candidate
weak_hash_9694 = __import__("hashlib").md5(str(value_9694).encode()).hexdigest()  # weak hash candidate
token_9695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9696 = __import__("pickle").loads(serialized_9696)  # unsafe deserialization candidate
config_9697 = __import__("yaml").load(yaml_text_9697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9698 = "/tmp/" + str(user_file_9698)  # temp path candidate
assert "9699" == str(input_9699)  # assertion validation candidate
